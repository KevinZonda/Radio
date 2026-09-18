#!/usr/bin/env python3
"""Radio 口播稿 TTS 合成（阿里云百炼 Qwen-Audio-TTS）。

用法：
    python synthesize.py                       # 合成默认口播稿（Rad1 script_v1.md）
    python synthesize.py -i 路径/稿件.md        # 合成其他 Markdown 稿件
    python synthesize.py --text "一句话"        # 单句冒烟测试，不读文件
    python synthesize.py --list                 # 只打印分段预览，不调用 API

前置：
    pip install -r requirements.txt
    API Key 放环境变量 DASHSCOPE_API_KEY，或写进本目录 .env 文件（已被 gitignore）

说明：
    - 【...】 制作提示行、引用块、标题、分隔线、Markdown 加粗都会被清除，它们不是口播文本
    - qwen-audio-3.0-tts-flash 支持行内情感标签（如 [serious]），可用 --tag 为每段加前缀
    - 按空行分段合成，输出 output/NN.mp3（每段一个，便于单句重录）+ output/full.mp3（拼好的整轨）
"""
import argparse
import os
import re
import sys
import threading
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_INPUT = REPO_ROOT / "Rad1-HCI_in Society" / "blog" / "script_v1.md"
DEFAULT_OUT = Path(__file__).resolve().parent / "output"

MODEL = "qwen-audio-3.0-tts-flash"


def load_env_file(path: Path) -> None:
    """Minimal .env loader (KEY=VALUE lines), does not override real env vars."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def extract_spoken_text(md_text: str) -> list[str]:
    """把口播稿 Markdown 切成口播段落列表。"""
    paragraphs, current = [], []
    for raw in md_text.splitlines():
        line = raw.strip()
        if not line or line == "---":
            if current:
                paragraphs.append("".join(current))
                current = []
            continue
        if line.startswith("【") or line.startswith(">") or line.startswith("#"):
            continue  # 制作提示 / 用法说明 / 标题：不读出声
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)          # 去加粗
        line = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", line)       # 去链接，留文字
        line = line.replace("`", "")
        current.append(line)
    if current:
        paragraphs.append("".join(current))
    return [p for p in paragraphs if p.strip()]


def synthesize_paragraph(text: str, voice: str, rate: float, tag: str | None,
                         model: str = MODEL) -> bytes:
    """合成单段文本，返回 mp3 字节。失败抛异常（由调用方重试）。"""
    import dashscope
    from dashscope.audio.tts_v2 import AudioFormat, ResultCallback, SpeechSynthesizer

    payload = f"{tag}{text}" if tag else text
    done = threading.Event()
    chunks: list[bytes] = []
    errors: list[str] = []

    class Callback(ResultCallback):
        def on_open(self):
            pass

        def on_data(self, data: bytes) -> None:
            chunks.append(data)

        def on_complete(self):
            done.set()

        def on_error(self, message: str):
            errors.append(message)
            done.set()

        def on_close(self):
            done.set()

        def on_event(self, message):
            pass

    synthesizer = SpeechSynthesizer(
        model=model,
        voice=voice,
        format=AudioFormat.MP3_24000HZ_MONO_256KBPS,
        speech_rate=rate,
        callback=Callback(),
    )
    synthesizer.call(payload)
    if not done.wait(timeout=300):
        raise TimeoutError(f"合成超时：{text[:20]}…")
    if errors:
        raise RuntimeError(errors[0])
    return b"".join(chunks)


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="合成口播稿为 mp3")
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_INPUT, help="口播稿 Markdown 路径")
    parser.add_argument("-o", "--out", type=Path, default=DEFAULT_OUT, help="输出目录")
    parser.add_argument("--voice", default="longanhuan_v3.6", help="音色，默认 longanhuan_v3.6")
    parser.add_argument("--model", default=MODEL, help="模型，默认 qwen-audio-3.0-tts-flash")
    parser.add_argument("--rate", type=float, default=1.0, help="语速倍率，默认 1.0")
    parser.add_argument("--tag", default=None, help='情感标签，如 "[serious]"，加在每段开头')
    parser.add_argument("--text", default=None, help="直接合成该句（冒烟测试），忽略 -i")
    parser.add_argument("--list", action="store_true", help="只打印分段预览")
    args = parser.parse_args()

    load_env_file(Path(__file__).resolve().parent / ".env")
    if not os.environ.get("DASHSCOPE_API_KEY"):
        sys.exit("缺少 DASHSCOPE_API_KEY：请设置环境变量或写入 src/tts/.env")

    paragraphs = [args.text] if args.text else extract_spoken_text(
        args.input.read_text(encoding="utf-8"))

    print(f"共 {len(paragraphs)} 段，模型 {args.model}，音色 {args.voice}，语速 x{args.rate}"
          + (f"，情感标签 {args.tag}" if args.tag else ""))
    for i, p in enumerate(paragraphs, 1):
        print(f"  {i:02d}. {p[:40]}{'…' if len(p) > 40 else ''}")
    if args.list or not paragraphs:
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    full = bytearray()
    for i, p in enumerate(paragraphs, 1):
        audio = None
        for attempt in (1, 2):
            try:
                audio = synthesize_paragraph(p, args.voice, args.rate, args.tag, args.model)
                break
            except Exception as e:  # noqa: BLE001 - 网络类错误重试一次
                print(f"  [warn] 第 {i} 段第 {attempt} 次尝试失败：{e}", file=sys.stderr)
                time.sleep(2 * attempt)
        if audio is None:
            sys.exit(f"第 {i} 段合成失败，已中止。已生成的段落保留在 {args.out}")
        (args.out / f"{i:02d}.mp3").write_bytes(audio)
        full.extend(audio)
        print(f"  {i:02d}.mp3  {len(audio) / 1024:.0f} KB")
    (args.out / "full.mp3").write_bytes(full)
    print(f"完成：{args.out / 'full.mp3'}（{len(full) / 1024 / 1024:.1f} MB）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
