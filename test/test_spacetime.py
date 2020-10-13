#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/9/25 14:20
# @file     : test_spacetime.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np

from rkm.basic.spacetime import SpaceTime


space = SpaceTime({
    "x": {
        "span": [0, 2 * np.pi],
        "step": 10
    },
    "y": {
        "span": [0, 2 * np.pi],
        "delta": 2 * np.pi / 8
    },
    "fft": True
})

print(space)

print(f'{space["x"].seq=}')
print(f'{space["y"].seq=}')

print(f'{space["x"].grid=}')
print(f'{space["y"].grid=}')

print(f'{space["x"].freq=}')
print(f'{space["y"].freq=}')
