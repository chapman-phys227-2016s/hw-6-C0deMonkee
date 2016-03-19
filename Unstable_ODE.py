#! /usr/bin/env python

"""
File: Unstable_ODE.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: C.4 *BOOM*
Date: March 18
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Oscillatory behavior in an ODE
"""
import numpy as np
import matplotlib.pyplot as plt

def run(alpha, t, e0):
    ans = Euler(alpha, 0, 100, e0, t)
    plt.plot(ans[1], ans[0])
    plt.show()
    plt.clf()
def Euler(alpha, xa, xb, ya, h):
    ans = []
    x_array = []
    x = xa
    x_array.append(x)
    y = ya
    ans.append(y)
    while x < xb:
        y += h * alpha * y
        ans.append(y)
        x += h
        x_array.append(x)
    return ans, x_array