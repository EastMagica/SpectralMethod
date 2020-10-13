#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/8/6 16:50
# @file     : erk.py.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np
from nodepy import rk


def erk_step(t0, u0, dt, f, rkbt, args):
    s = len(rkbt)
    k = np.zeros((s, *u0.shape), dtype=u0.dtype)
    for i in range(s):
        k[i, ...] = f(
            t0 + rkbt.c[i] * dt,
            # u0 + dt * rkbt.A[i, ...] @ k,
            u0 + dt * np.sum(k * rkbt.A[i, ...].reshape(s, 1, 1), axis=0),
            *args
        )
    # u1 = u0 + dt * rkbt.b @ k
    u1 = u0 + dt * np.sum(k * rkbt.b.reshape(s, 1, 1), axis=0)
    return u1


def erk(u0, f, t_eval, method="RK44", args=()):
    rkbt = rk.loadRKM(method).__num__()
    u = np.zeros(
        (t_eval.size, *u0.shape),
        dtype=u0.dtype
    )
    u[0, ...] = u0
    t_step = len(t_eval) - 1
    rate = 20
    for k, t1 in enumerate(t_eval[1:], start=1):
        t_percent = np.int(np.around(k / t_step * rate))
        print("\r[{}{}]({}/{})".format(
            "#" * t_percent,
            "+" * (rate - t_percent),
            k, t_step
        ), end="")

        t0 = t_eval[k - 1]
        dt = t1 - t0
        u[k, ...] = erk_step(
            t0, u[k - 1, ...], dt, f, rkbt, args
        )

    print()
    return u
