#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/12/17 14:34
# @file     : run.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib import animation

from rkm.erk import erk
from rkm.plot import imshow_2d, imshow_scroll

from basic_func import spec_rhs, exact_solution


# Spatial Discretization
# -----------------------

Lx = 10

nx = 512

x_span = np.array([-Lx / 2, Lx / 2])
x_eval = np.linspace(*x_span, nx + 1)[:-1]

kx = (2 * np.pi / Lx) * np.fft.fftfreq(nx) * nx


# Time Discretization
# --------------------

dt = 0.001

t_span = np.array([0, 20.])

t_eval = np.arange(
    t_span[0], t_span[1] + dt, dt
)


# Initial Conditions
# -------------------

w = exact_solution(0., x_eval)

wt = np.fft.fft(w)


# Solve ODEs
# -----------

# Constant Time Step
ww = erk(
    wt, spec_rhs, t_eval,
    args=(kx, ),
    method="RK44"
)


w = np.array([
    np.fft.ifft(ww[i, ...]).real
    for i, v in enumerate(t_eval)
])


# Plot Data
# ----------

# imshow_2d(
#     np.flipud(w), t_eval,
#     (*x_span, *t_span)
# )

# imshow_scroll(
#     w, t_eval, x_eval,
#     (*x_span, *t_span),
#     rate=0.01
# )

w = w[::40, ...]
t_eval = t_eval[::40]

fig, ax = plt.subplots(figsize=(6.5, 5.5))
ax.set_title(
    # r"$u_t+u\partial_x u-\frac{1}{10}\partial^2_{x}u$",
    r"$u_t+u\partial_x u$",
    weight='normal',
    family='serif',
    color='black',
    size=16,
)
ln, = ax.plot(x_eval, w[0, :], marker=".", animated=True)
tx = ax.text(
    2.5, 1.75,
    "t={:2.3f}".format(t_eval[0]),
    fontsize=10, ha="center"
)
ax.text(
    0, 1.85,
    "Solved by Pesudospectral with RK44".format(t_eval[0]),
    fontsize=10, ha="center"
)


def init():
    ax.set_xlim(*x_span)
    ax.set_ylim(-0.05, 2.)
    return ln,


def animate(i):
    ln.set_data(x_eval, w[i, :])
    tx.set_text("t={:2.3f}".format(t_eval[i]))
    return ln,


animation = animation.FuncAnimation(
    fig=fig, func=animate, frames=300, init_func=init, interval=20, blit=False
)
animation.save('redraw.gif', writer='imagemagick')
