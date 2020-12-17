#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/12/17 14:34
# @file     : basic_func.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np


eta = 0.1

# RHS Equation
# -------------

# not convert stiffness
def spec_rhs(tspan, wt, kx):
    w = np.fft.ifft(wt).real
    wx = np.fft.ifft(1j * kx * wt).real
    wx2 = -kx**2 * wt

    # rhs = -np.fft.fft(w * wx) + eta * wx2
    rhs = -np.fft.fft(w * wx)

    return rhs


# def g(k, t):
#     return np.exp(-1j * k**3 * t)
#
#
# def spec_rhs(t0, vt, kx):
#     # print("t={:.4f}".format(t0))
#     gg = g(kx, t0)
#
#     rhs = - gg * np.fft.fft(np.fft.ifft(vt / gg).real * np.fft.ifft(1j * kx * vt / gg).real)
#
#     # print(f"{rhs=}")
#
#     return rhs


# Exact/Initial Solution
# -----------------------

def exact_solution(t, x):
    """
    Exact solition Solution.

    Parameters
    ----------
    t
    x
    mode
    """
    return 1 / (1 + x**2)
