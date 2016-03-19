#! /usr/bin/env python

"""
File: yx ODE.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: C.3
Date: March 17
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Solves an ODE problem using the forward Euler method
"""
import numpy as np
import matplotlib.pyplot as plt

def Euler(f, xa, xb, ya, h):
    ans = []
    x_array = []
    x = xa
    x_array.append(x)
    y = ya
    ans.append(y)
    while x < xb:
        y += h * f(y)
        ans.append(y)
        x += h
        x_array.append(x)
    return ans, x_array
def func(x):
    return 1/(2.0 *(x - 1))
def ans(x):
    return 1 + np.sqrt(x+1e-3)
def run():
    ans1 = Euler(func, 0, 4, 1 + np.sqrt(1e-3), 1)
    ans2 = Euler(func, 0, 4, 1 + np.sqrt(1e-3), 0.25)
    ans3 = Euler(func, 0, 4, 1 + np.sqrt(1e-3), 0.01)
    x = np.linspace(0,4,1000)
    y = ans(x)
    plt.plot(ans1[1], ans1[0])
    plt.plot(ans2[1], ans2[0])
    plt.plot(ans3[1], ans3[0])
    plt.plot(x, y)