#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:25:48 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt

F = open("FINAL_PUL_FUN.txt", "r")
O1 = open("FINAL_PUL_1O.txt", "r")
O2 = open("FINAL_PUL_2O.txt", "r")
O3= open("FINAL_PUL_3O.txt", "r")

F_array = np.array([])
F_RADIUS = np.array([])
F_R = np.array([])
F_P = np.array([])
for i in F:
    F_array = np.append(F_array, i)
    F_RADIUS = np.append(F_RADIUS, float(i[7:15]))
    F_R = np.append(F_R, float(i[16:22])* (10**(float(i[23:26]))))
    F_P = np.append(F_P, float(i[27:34])* (10**(float(i[35:38]))))

O1_array = np.array([])
O1_RADIUS = np.array([])
O1_R = np.array([])
O1_P = np.array([])
for i in O1:
    O1_array = np.append(O1_array, i)
    O1_RADIUS = np.append(O1_RADIUS, float(i[7:15]))
    O1_R = np.append(O1_R, float(i[16:22])* (10**(float(i[23:26]))))
    O1_P = np.append(O1_P, float(i[27:34])* (10**(float(i[35:38]))))

O2_array = np.array([])
O2_RADIUS = np.array([])
O2_R = np.array([])
O2_P = np.array([])
for i in O2:
    O2_array = np.append(O2_array, i)
    O2_RADIUS = np.append(O2_RADIUS, float(i[7:15]))
    O2_R = np.append(O2_R, float(i[16:22])* (10**(float(i[23:26]))))
    O2_P = np.append(O2_P, float(i[27:34])* (10**(float(i[35:38]))))

O3_array = np.array([])
O3_RADIUS = np.array([])
O3_R = np.array([])
O3_P = np.array([])
for i in O3:
    O3_array = np.append(O3_array, i)
    O3_RADIUS = np.append(O3_RADIUS, float(i[7:15]))
    O3_R = np.append(O3_R, float(i[16:22])* (10**(float(i[23:26]))))
    O3_P = np.append(O3_P, float(i[27:34])* (10**(float(i[35:38]))))

 
plt.figure(figsize=(7,5))
plt.plot(F_RADIUS[:99], F_R[:99], label="Fundamental")
plt.plot(O1_RADIUS[:99], O1_R[:99], label="First Overtone")
plt.plot(O2_RADIUS[:99], O2_R[:99], label="Second Overtone")
plt.plot(O3_RADIUS[:99], O3_R[:99], label="Third Overtone")
plt.xlabel(r'r/$R_{star}$',fontsize=16)
plt.ylabel(r'$\delta$r/ r',fontsize=16)
plt.legend()
plt.savefig("R.png")
"""
plt.figure(figsize=(7,5))
plt.plot(F_RADIUS[:99], F_P[:99], label="Fundamental")
plt.plot(O1_RADIUS[:99], O1_P[:99], label="First Overtone")
plt.plot(O2_RADIUS[:99], O2_P[:99], label="Second Overtone")
plt.plot(O3_RADIUS[:99], O3_P[:99], label="Third Overtone")
plt.xlabel(r'r/$R_{star}$',fontsize=16)
plt.ylabel(r'$\delta$P/ P',fontsize=16)
plt.legend()
plt.savefig("P.png")
"""