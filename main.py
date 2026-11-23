"""Sum up 23 November's world news in one image.

The program copies the front-page image held in this repository to
/output/entry.png. No network, no randomness, no input: two runs write
the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> None:
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png is missing from the repository")
    if os.path.getsize(SOURCE) > 1024 * 1024:
        raise SystemExit("entry.png must be at most 1 MiB")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, "/output/entry.png")


if __name__ == "__main__":
    main()
