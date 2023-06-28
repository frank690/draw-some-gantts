"""
This file contains all the scripts that are used in this repository.
"""

__all__ = ["read_data", "create_timeline", "save_timeline"]


import json
from typing import Tuple

import pandas as pd
import plotly.express as px

from draw_some_gantts.constants import COLORS


def read_data(path: str) -> Tuple[str, pd.DataFrame]:
    """
    Read the json source file..
    :param path: path to the json file
    :return: extracted date str and pandas dataframe
    """
    with open(path, "r") as f:
        data = json.load(f)
    return data["date"], pd.DataFrame(data["tasks"])


def create_timeline(df: pd.DataFrame, date: str) -> px.timeline:
    """
    Use the given pandas dataframe to create a plotly timeline.
    :param df: pandas dataframe
    :param date: date as string that will be set as the title of the plotly timeline
    :return: plotly express timeline object
    """
    fig = px.timeline(
        df,
        title=date,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="State",
        color_discrete_map=COLORS,
    )
    fig.update_yaxes(autorange="reversed")
    return fig


def save_timeline(fig: px.timeline, path: str) -> None:
    """
    Save the given plotly timeline to the given path.
    :param fig: plotly express timeline object
    :param path: path to output file
    """
    fig.write_image(path, width=1200, height=600)
