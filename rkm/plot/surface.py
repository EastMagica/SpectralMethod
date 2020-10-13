#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/28 14:16
# @file     : surface.py
# @project  : SpectralMethod
# @software : PyCharm

import matplotlib.pyplot as plt


def wireframe(ax, x, y, z):
    ax.plot_wireframe(
        x, y, z,
        # cmap=cm.coolwarm,
        rstride=20,
        cstride=20,
        # linewidth=0,
        # antialiased=False
    )

    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("t", fontsize=15)
    ax.set_zlabel("w", fontsize=15)

    plt.show()