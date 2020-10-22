# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:17:37 2020

@author: christian
"""
import numpy as np

def calcV_(n,U,phase,m=12):
    q = 1.6e-19
    u = 1.6e-27
    v = np.sqrt( 2 * n * q * np.sin(phase) * U / m / u)
    return v


def calcV(U,n,phase,m=12):
    q = 1.6e-19
    u = 1.6e-27
    v = np.sqrt( 2 * n * q * np.sin(phase) * U / m / u)
    return v

# Energy of the Atom = n * q * U = 0.5 * m * v^2
# v^2 = 2 * n * q * U / m = 2 * n * q * U / 12 / u
# lithium like: +1q

c = 3e8 # m/s
N = 20
U = 3000 # V
F = 2e6 # Hz
tTube = 0.5 * 1/F
lGap = 0.001 # m
v0 = 0 # m/s
phase = 80/180*np.pi

E = N*U # eV
print('Total energy %.1f eV'%E)

V = calcV(U,N,phase) + v0
print(V/c)
# V/c << 1, keine relativistische Rechnung

# n = 1:n
n = np.arange(1,N+1)

v = calcV(U,n,phase) + v0
s = v * tTube
#print(s)
print('total length %.2fm'%np.sum(s))

lTube = s - lGap
print('length of the tubes [m]')
print(lTube)


# vfunc = np.vectorize(calcV_)
# tmp = vfunc(n,U,phase)
# print(tmp)

