#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/12/17 15:34
# @file     : animation.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def init():
    return ax.plot(x, np.sin(x))


def animate(i):
    try:
        ax.lines.pop(1)
    except Exception:
        pass
    line = ax.plot(x, np.sin(x + i / 10.0), 'r')
    return line,