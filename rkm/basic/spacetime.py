#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author   : east
# @time     : 2020/9/25 12:25
# @file     : solver.py
# @project  : SpectralMethod
# @software : PyCharm

import abc

import numpy as np


# Functions
# =========

def space_time(options):
    """

    options: {
        "x": {
            "seq": None,
            "span": None,
            "step": None,
            "delta": None
        },
        "y": {
            ...
        },
        "fft": False
    }

    Parameters
    ----------
    options: dict

    Returns
    -------
    dict
    """
    is_fft = options.pop("fft", False)

    dims = dict()
    ndims = len(options)

    # Init Dimensions
    for label, value in options.items():
        dims[label] = (
            SequenceDiscrete(
                fft=is_fft, **value
            )
        )

    # If Dimensions > 1, generate mesh grid
    if ndims > 1:
        grid_ndim = np.meshgrid(
            *[item.seq for item in dims.values()]
        )
        for i, k in enumerate(dims.keys()):
            dims[k].seq = grid_ndim[i]

    # If using FFT, generate fft frequencies
    if is_fft is True:
        freq_ndim = np.meshgrid(
            *[item.freq for item in dims.values()]
        )
        for i, k in enumerate(dims.keys()):
            dims[k].freq = freq_ndim[i]

    if ndims == 1:
        return dims.popitem()[1]
    else:
        return dims


# Classes
# =======

class SequenceDiscrete(object):
    def __init__(self, fft=False, **options):
        self.span = None
        self.step = None
        self.delta = None
        self.length = None
        self.seq = None
        self.freq = None

        self.discrete(
            last=options.pop("last", False), **options
        )
        self.fftfreq(isfft=fft)

    def fftfreq(self, isfft=False):
        """FFT Freq

        Parameters
        ----------
        isfft: bool
        """
        if isfft is True:
            self.freq = (2 * np.pi / self.length) * np.fft.fftfreq(self.step) * self.step

    def discrete(self, last=False, span=None, step=None, delta=None, seq=None):
        """

        - span + step
        - span + delta
        - step + delta
        - seq

        Parameters
        ----------
        last
        span: ndarray or list
            with 2 length, [start, end].
        step: int
            with n+1 length, [0, 1, 2, ..., n]
        delta: float
            with n+1 length, [t0, t0+1*dt, ..., t0+n*dt]
        seq: ndarray or list
            with n+1 length, [t0, t1, ..., tn]
        """
        if seq:
            self.seq = np.asarray(seq)
            self.step = len(self.seq)
            self.delta = self.seq[1] - self.seq[0]
            self.span = np.array([self.seq[0], self.seq[-1]+self.delta])
            self.length = self.span[1] - self.span[0]
        elif span:
            self.span = np.asarray(span)
            self.length = self.span[1] - self.span[0]
            if step:
                self.step = int(step)
                self.delta = self.length / self.step
            elif delta:
                self.delta = np.float(delta)
                self.step = int(self.length / self.delta)
            else:
                raise ValueError("Incomplete conditions")
            self.seq = np.linspace(*self.span, self.step + 1)
        elif step and delta:
            self.step = int(step)
            self.delta = np.float(delta)
            self.span = np.array([0, delta * step])
            self.length = self.span[1] - self.span[0]
            self.seq = np.linspace(*self.span, self.step + 1)
        else:
            raise ValueError("Incomplete conditions")

        # Note: Remove End Time
        if last is False:
            self.seq = self.seq[:-1]

