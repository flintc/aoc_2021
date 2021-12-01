import itertools as it
import json
import math
import operator as op
import os
import re
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests


def get_input(day, year=2021, cache_dir=None):
    """
    Get the input for day `day`
    """
    if cache_dir is None:
        cache_dir = Path(__file__).parent
    elif not isinstance(cache_dir, Path):
        cache_dir = Path(cache_dir)
    cache_file = cache_dir / f'day{day}.txt'
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return f.read()
    else:
        resp = requests.get(
          f"https://adventofcode.com/{year}/day/{day}/input",
          cookies={"session": os.environ["AOC_SESSION"]}
        )
        if resp.status_code != 200:
            raise Exception(f"Failed to get input for day {day}")
        with open(cache_file, 'w') as f:
            f.write(resp.text)
        return resp.text
