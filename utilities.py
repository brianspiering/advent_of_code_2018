#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Helper functions for Advent of Code
"""

from typing import List

def load_input(day: int) -> List[str]:
    with open(f'./input/day_{day:02}.txt') as f:
        data = f.read().splitlines()
    return data