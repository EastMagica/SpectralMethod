#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/27 21:49
# @file     : run.py.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from rkm.erk import erk
from rkm.plot import imshow_2d, imshow_scroll

from basic_func import spec_rhs, exact_solution, g


# Spatial Discretization
# -----------------------

Lx = 100 * np.pi

nx = 512

x_span = np.array([-Lx / 2, Lx / 2])
x_eval = np.linspace(*x_span, nx + 1)[:-1]

kx = (2 * np.pi / Lx) * np.fft.fftfreq(nx) * nx


# Time Discretization
# --------------------

dt = 0.01

t_span = np.array([0, 500.])

t_eval = np.arange(
    t_span[0], t_span[1] + dt, dt
)


# Initial Conditions
# -------------------

w = exact_solution(0., x_eval, mode=2)

wt = np.fft.fft(w)

# around numerical stiffness
# 1. standard integrating factor method
vt = wt / g(kx, 0.)


# Solve ODEs
# -----------


# # Adaptive Time Step
# sol = solve_ivp(
#     spec_rhs, t_span, vt, t_eval=t_eval,
#     method="RK45", args=(kx, )
# )
#
# ww = sol.y.T


# Constant Time Step
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
    (*x_span, *t_span)
)

# imshow_scroll(
#     w, t_eval,
#     (*x_span, *t_span),
#     rate=0.01
# )
