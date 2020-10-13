#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/28 16:56
# @file     : basic_func.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np


# Constant
# ---------

lamd = 1.
eps = 1.


# RHS Equation
# -------------

def spec_rhs(t, wt, kx, ky, kderv):
    wt2 = wt.reshape(kx.shape)

    w2 = np.fft.ifft2(wt2).real

    rhs = - lamd * eps**2 * kderv * wt2 - lamd * np.fft.fft2(w2**3) + lamd * wt2

    return rhs.reshape(-1)


# # Standard Integrate factor
# # Not used in this question
# def g(t, kx, ky):
#     return np.exp(
#         lamd * (epsilon**2 * (kx**2 + ky**2) - 1.) * t
#     )
#
#
# def spec_rhs(t, vt, kx, ky):
#     print(t)
#     vt = vt.reshape(kx.shape)
#     gg = g(t, kx, ky)
#
#     phit = vt / gg
#     phi = np.fft.ifft2(phit).real
#
#     rhs = - lamd * gg * np.fft.fft2(phi**3)
#
#     return rhs.flatten()


# Exact/Initial Solution
# -----------------------

def init_value(t, x, y, mode="random", **kwargs):
    u = np.zeros(x.shape)

    if mode == "random":
        rand = np.random.random(x.shape)
        u[rand >= 0.5] = -1
        u[rand < 0.5] = 1
    elif mode == "sin":
        u = np.sin(0.05 * x) * np.sin(0.05 * y)
    elif mode == "round":
        u = - np.ones(x.shape, dtype=np.float)
        round_center = (x[0, x.shape[1] // 2], y[y.shape[0] // 2, 0])
        round_r = kwargs["r"]
        u[(x-round_center[0])**2 + (y-round_center[1])**2 < round_r**2] = 1.
    else:
        raise ValueError

    return u
