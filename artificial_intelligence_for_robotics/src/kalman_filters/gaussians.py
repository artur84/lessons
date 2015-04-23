'''
Created on 23/04/2015

@author: Arturo Escobedo
'''
from math import *

def f(mu, sigma2, x):
    return 1 / sqrt(2 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)

if __name__ == '__main__':
    print f(10., 4., 8.)
