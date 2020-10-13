#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/8/7 22:12
# @file     : run.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np

from rkm.erk import erk
from rkm.plot import imshow_2d, imshow_scroll


r"""

.. math::

    \frac{\mathrm{d}\phi}{\mathrm{d}t}=\Delta\phi

"""

# Spatial Discretization
# -----------------------

Lx = 10
nx = 64

x_span = np.array([- Lx / 2, Lx / 2])
x = np.linspace(*x_span, nx+1)[:-1]

kx = (2 * np.pi / Lx) * np.fft.fftfreq(nx) * nx


# Time Discretization
# --------------------

dt = 0.1

t_span = np.array([0., 100.])

t_eval = np.arange(
    t_span[0], t_span[1]+dt, dt
)


# Initial Conditions
# -------------------

w = np.exp(-x**2)

wt = np.fft.fft(w)


def spec_rhs(t0, wt0, k):
    # Wave Equation
    # return - 1j * k * wt0
    # Burgers
    nu = 0.03
    w0 = np.fft.ifft(wt0).real
    w0_x = np.fft.ifft(1j * k * wt0).real
    return - np.fft.fft(w0 * w0_x) - nu * k**2 * wt0
    # return - k**2 * wt0

# Solve Ode
# ----------

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

imshow_scroll(
    w, t_eval,
    (*x_span, *t_span),
    rate=-1
)
