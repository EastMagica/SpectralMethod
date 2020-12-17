#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/7/28 14:14
# @file     : image.py
# @project  : SpectralMethod
# @software : PyCharm

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1 import make_axes_locatable


def imshow_2d(u, t, extent=None):
    fig, ax = plt.subplots(figsize=(6.5, 5.5))

    im = ax.imshow(u, aspect="auto", extent=extent)

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="2%", pad=0.05)

    fig.colorbar(im, cax=cax)

    ax.set_xlabel("X", fontsize=15)
    ax.set_ylabel("T", fontsize=15)

    plt.show()


def imshow_3d(u, t, extent=None):
    fig, ax = plt.subplots(figsize=(6.5, 5.5))

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="2%", pad=0.05)

    ax.set_xlabel("X", fontsize=15)
    ax.set_ylabel("Y", fontsize=15)

    i = 0
    while True:
        ax.cla()
        cax.clear()

        im = ax.imshow(u[i, ...], aspect="auto", extent=extent)
        fig.colorbar(im, cax=cax)

        ax.set_title("time: {:.4f}".format(t[i]))

        i = (i + 1) % (len(t) - 1)

        plt.pause(0.1)


class IndexTracker:
    def __init__(self, fig, ax, u, t_eval, x_eval=None, extent=None, rate=1e-2):
        self.fig = fig
        self.ax = ax

        self.extent = extent
        self.ind = 0

        self.u = u
        self.t_eval = t_eval
        self.ndim = u.ndim
        self.slices = u.shape[0]

        if rate == -1:
            self.rate = 1
        else:
            self.rate = int(rate * self.slices)

        self.x_eval = np.arange(self.u[0, ...].size) if x_eval is None else x_eval

        self.im = None

        if self.ndim == 3:
            divider = make_axes_locatable(ax)
            self.cax = divider.append_axes("right", size="2%", pad=0.05)
        elif self.ndim == 2:
            self.max_u = np.max(self.u)
            self.min_u = np.min(self.u)
            self.d_u = self.max_u - self.min_u

        self.update()

    def on_scroll(self, event):
        print("%s %s" % (event.button, event.step))
        step = int(event.step)
        self.ind = (self.ind - step * self.rate) % self.slices
        self.update()

    def update(self):
        self.ax.cla()
        if self.ndim == 3:
            self.im = self.ax.imshow(
                self.u[self.ind, ...],
                extent=self.extent
            )
            self.update_colorbar()
        elif self.ndim == 2:
            self.im = self.ax.plot(
                self.x_eval,
                self.u[self.ind, ...],
                marker="."
            )[0]
            self.ax.set_ylim(
                self.min_u - 0.05 * self.d_u,
                self.max_u + 0.1 * self.d_u,
            )
        self.update_label()
        self.im.axes.figure.canvas.draw()

    def update_colorbar(self):
        self.cax.clear()
        self.fig.colorbar(self.im, cax=self.cax)

    def update_label(self):
        self.ax.set_xlabel('X')
        if self.ndim == 3:
            self.ax.set_ylabel('Y')
        elif self.ndim == 2:
            self.ax.set_ylabel('T')
        else:
            raise ValueError
        self.ax.set_title("time: {:.4f}".format(self.t_eval[self.ind]))


def imshow_scroll(u, t_eval, x_eval=None, extent=None, rate=1e-2):
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    tracker = IndexTracker(fig, ax, u, t_eval, x_eval=x_eval, extent=extent, rate=rate)
    fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
    plt.show()

