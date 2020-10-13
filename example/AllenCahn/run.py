#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/28 16:56
# @file     : run.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np

import matplotlib.pyplot as plt

from rkm.erk import erk
from rkm.plot import imshow_3d, imshow_scroll

from basic_func import spec_rhs, init_value


# Spatial discretization
# -----------------------

# Lx = 256
# Ly = 256

# # Domain too small
Lx = 50 * np.pi
Ly = 50 * np.pi

nx = 128
ny = 128

x_span = np.array([0., Lx])
y_span = np.array([0., Ly])

x = np.linspace(*x_span, nx + 1)[:-1]
y = np.linspace(*y_span, ny + 1)[:-1]

x, y = np.meshgrid(x, y)

kx = (2 * np.pi / Lx * 2) * np.fft.fftfreq(nx) * nx
ky = (2 * np.pi / Ly * 2) * np.fft.fftfreq(ny) * ny

kx, ky = np.meshgrid(kx, ky)

kderv = kx**2 + ky**2


# Time discretization
# --------------------

dt = 0.01

t_span = np.array([0, 10.])

t_eval = np.arange(
    t_span[0], t_span[1] + dt,
    dt
)


# Initial Conditions
# -------------------

w2 = init_value(0., x, y, mode="random")

wt2 = np.fft.fft2(w2)
wt1 = wt2.flatten()

sol = np.zeros((t_eval.size + 1, nx, ny), dtype=np.float)
sol[0, ...] = w2.copy()


# Solve ODEs
# -----------

# # Adaptive Time Step
# sol = solve_ivp(
#     spec_rhs, t_span, wt1, t_eval=t_eval,
#     method="RK45", args=(kx, ky, kderv)
# )
#
# ww = sol.y.T


# Constant Time Step
ww = erk(
    wt1, spec_rhs, t_eval,
    args=(kx, ky, kderv),
    method="RK44"
)


w = np.array([
    np.fft.ifft2(ww[i, ...].reshape(nx, ny)).real
    for i, v in enumerate(t_eval)
])


# Plot Data
# ----------

imshow_scroll(
    w, t_eval,
    (*x_span, *y_span)
)
