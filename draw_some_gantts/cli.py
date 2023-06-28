"""
This module contains functionality for the cli of this repository.
"""

from argparse import ArgumentParser


def parse():
    parser = ArgumentParser(
        description="draw-some-gantts. "
        "ADraws some gantt charts from given json data.",
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        help="Path to output (svg) file that will be created / show the gantt chart.",
    )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        type=str,
        help="Path to source (json) file that will be used to create the gantt chart.",
    )

    args, _ = parser.parse_known_args()

    return args
