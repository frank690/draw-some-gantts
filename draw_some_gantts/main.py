"""
Main module to run the buffalo-inspection
"""

__all__ = [
    "start",
]

import sys

from draw_some_gantts.cli import parse
from draw_some_gantts.scripts import create_timeline, read_data, save_timeline


def run(file: str, output: str):
    """
    Run the script to read the given file and generate a gantt chart to output.
    """
    try:
        print("Generating gantt chart...")
        print(f"Reading file {file}...")
        date, df = read_data(path=file)

        print("Generating gantt chart ...")
        timeline = create_timeline(df=df, date=date)

        print(f"Saving to {output}...")
        save_timeline(fig=timeline, path=output)

        print("Process done.")
        sys.exit(0)
    except Exception:
        print("Unexpected error:", sys.exc_info())
        print(f"file: {file}, output: {output}")
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
