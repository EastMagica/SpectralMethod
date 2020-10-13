#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/28 14:39
# @file     : basic_func.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np


# RHS Equation
# -------------

def g(k, t):
    return np.exp((k**4 - k**2) * t)


def spec_rhs(t0, vt, kx):
    # print("tspan:", tspan)
    gg = g(kx, t0)

    wt = vt / gg
    w = np.fft.ifft(wt).real
    w_x = np.fft.ifft(1j * kx * wt).real

    rhs = - gg * np.fft.fft(w * w_x)

    return rhs


# Exact Solution
# ---------------

def exact_solution(t, x, L):
    return np.cos(x/L) * (1 + np.sin(x / L))
