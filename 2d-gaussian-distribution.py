#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:21:16 2022

@author: Anh Viet Pham
"""

from matplotlib import cm
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt


def gkernel(l=3, sig=2):
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sig))

    return kernel / np.sum(kernel)


N = 60
X = np.linspace(-2, 2, N)
Y = np.linspace(-2, 2, N)
g_kernel = gkernel(3, 1)

x = np.linspace(-2, 2, num=3)
y = np.linspace(-2, 2, num=3)

x, y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, g_kernel, cmap=cm.jet)
plt.show()
