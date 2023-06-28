"""
Main module to run the buffalo-inspection
"""

__all__ = [
    "start",
]

import sys
from typing import Optional

from draw_some_gantts.cli import parse
from draw_some_gantts.scripts import create_timeline, read_data


def run(file: Optional[str], output: Optional[str]):
    """
    Run the script to read the given file and generate a gantt chart to output.
    """
    try:
        print("Generating gantt chart...")

        if file is None:
            print("No source file given. Falling back to example file.")
            file = "./data/example.json"

        if output is None:
            print("No output given. Falling back to example output.")
            output = "./output/example.png"

        print(f"Reading file {file}...")
        date, df = read_data(path=file)

        print(f"Generating gantt chart to {output}...")
        create_timeline(df=df, date=date)

        print("Process done.")
        sys.exit(0)
    except Exception:
        print("Unexpected error:", sys.exc_info())
        sys.exit(1)


def start():
    """
    Starting point for regular (CLI) usage.
    """
    args = parse()

    run(
        file=args.file,
        output=args.output,
    )


if __name__ == "__main__":
    start()
