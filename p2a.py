#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 04:32:26 2019

@author: constanzamunoz
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


masa = np.array([1, 3, 15])
P = np.array([1.482*1e17, 1.141*1e17, 2.769*1e16])
T = np.array([1.442*1e7, 2.347*1e7, 3.275*1e7])
R = np.array([6.932*1e10, 1.276*1e11, 3.289*1e11])
L = np.array([0.9083, 98.35, 1.96*1e4])


f_m = interpolate.interp1d(masa, P)
f_t = interpolate.interp1d(masa, T)
f_r = interpolate.interp1d(masa, R)
f_L = interpolate.interp1d(masa, L, kind="quadratic")
#f(m6.5)

xvals = np.linspace(1, 16, 100)
l=np.interp(xvals, masa, L)