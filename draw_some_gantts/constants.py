"""
This file contains all the constants that are used in this repository.
"""

__all__ = ["COLORS", "EXAMPLE_JSON_FILE", "EXAMPLE_OUTPUT_FILE"]

from pathlib import Path

COLORS = {
    "Not Started": "rgb(153, 0, 0)",
    "In Progress": "rgb(235, 235, 0)",
    "Completed": "rgb(0, 153, 0)",
}

EXAMPLE_JSON_FILE = (Path(__file__).parent.parent / "data" / "example.json").resolve()
EXAMPLE_OUTPUT_FILE = (
    Path(__file__).parent.parent / "output" / "example.html"
).resolve()
