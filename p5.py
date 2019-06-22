#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:56:20 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt

M1 = open("1M10L.txt", "r")
M15 = open("15M100L.txt", "r")


M1_RADIUS = np.array([])
M1_R = np.array([])
for i in M1: 
    M1_RADIUS = np.append(M1_RADIUS, float(i[7:15]))
    M1_R = np.append(M1_R, float(i[15:22])* (10**(float(i[23:26]))))
    

M15_RADIUS = np.array([])
M15_R = np.array([])
for i in M15: 
    M15_RADIUS = np.append(M15_RADIUS, float(i[7:15]))
    M15_R = np.append(M15_R, float(i[15:22])* (10**(float(i[23:26]))))
 
plt.figure(figsize=(7,5))
plt.plot(M1_RADIUS[:99], M1_R[:99], '.', color= "red", label="p-mode = 5")
plt.ylabel(r'$\xi_{r}$',fontsize=16)
plt.xlabel(r'r/$R_{star}$',fontsize=16)
plt.legend()
plt.savefig("pmode.png")
