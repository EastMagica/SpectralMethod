#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/27 21:54
# @file     : basic_func.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np


# RHS Equation
# -------------

# # not convert stiffness
# def spec_rhs(tspan, wt, kx):
#     w = np.fft.ifft(wt)
#     wx = np.fft.ifft(1j * kx * wt)
#
#     rhs = -np.fft.fft(w * wx) - 1j * kx**3 * wt
#
#     return rhs


def g(k, t):
    return np.exp(-1j * k**3 * t)


t_tmp = 0.0


def spec_rhs(t0, vt, kx):
    # print("t={:.4f}".format(t0))
    gg = g(kx, t0)

    rhs = - gg * np.fft.fft(np.fft.ifft(vt / gg).real * np.fft.ifft(1j * kx * vt / gg).real)

    return rhs


# Exact/Initial Solution
# -----------------------

def exact_solution(t, x, mode=1):
    """
    Exact solition Solution.

    Parameters
    ----------
    t
    x
    mode
    """
    if mode == 1:
        # Single Solitary Waves

        kk = 0.3
        x0 = 20

        return 12 * kk**2 * 1 / (np.cosh(kk * (x - x0) - 4 * kk**3 * t))**2

    elif mode == 2:
        # Five Solitary Waves

        kk = np.array([0.3, 0.25, 0.2, 0.15, 0.1])
        x0 = np.array([-120., -90., -60., -30., 0.])

        return np.sum([
            12 * kk[i] ** 2 * 1 / (np.cosh(kk[i] * (x - x0[i]))) ** 2
            for i in range(5)
        ], axis=0)

    else:

        raise ValueError

