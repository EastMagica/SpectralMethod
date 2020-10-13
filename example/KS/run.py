#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/28 14:39
# @file     : run.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from rkm.erk import erk
from rkm.plot import imshow_2d

from basic_func import spec_rhs, exact_solution, g


# Constant Value
# ---------------

L = 16
Lx = 2 * L * np.pi

nx = 128

x_span = np.array([0, Lx])
x = np.linspace(*x_span, nx + 1)[:-1]

kx = (2 * np.pi / Lx) * np.fft.fftfreq(nx) * nx
# kx[0] = 1e-6  # 避免 ZeroDivisionError


# Initial Conditions
# -------------------

w = exact_solution(0., x, L)

print("w0:", w)

wt = np.fft.fft(w)

gg = g(kx, 0.)

vt = wt * gg


# Solve ODEs
# -----------

dt = 1e-4

tspan = np.array([0, 100.])

t_eval = np.arange(
    tspan[0], tspan[1]+dt, dt
)

# sol = solve_ivp(
#     spec_rhs, tspan, vt, t_eval=t_eval,
#     method="RK45", args=(kx, )
# )
#
# w = np.array([
#     np.fft.ifft(sol.y[:, i] / g(kx, sol.t[i])).real
#     for i, v in enumerate(sol.t)
# ])

ww = erk(
    vt, spec_rhs, t_eval,
    args=(kx, ),
    method="RK44"
)

w = np.array([
    np.fft.ifft(ww[i, ...] / g(kx, t_eval[i])).real
    for i, v in enumerate(t_eval)
])

# Plot Data
# ----------

imshow_2d(
    np.flipud(w), t_eval,
    (*x_span, *tspan)
)

