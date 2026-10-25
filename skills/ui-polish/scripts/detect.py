"""Impeccable의 선택 실행 detector. 자동 설치나 다른 CLI 기능은 호출하지 않는다."""

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    engine = Path(__file__).resolve().parent / "bin" / "windows-x64" / "impeccable.exe"
    if not engine.is_file():
        print(f"Impeccable detector binary is missing: {engine}", file=sys.stderr)
        return 127
    environment = os.environ.copy()
    environment["DO_NOT_TRACK"] = "1"
    environment["IMPECCABLE_NO_TELEMETRY"] = "1"
    try:
        return subprocess.run([str(engine), "detect", *sys.argv[1:]], env=environment).returncode
    except OSError as error:
        print(f"Cannot start Impeccable detector: {error}", file=sys.stderr)
        return 127


if __name__ == "__main__":
    raise SystemExit(main())
