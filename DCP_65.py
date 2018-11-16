# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:39:25 2018
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

import numpy as np
from random import random_integers

x = np.random.random_integers(0, 20, (3,4))


def unroll(x) :
    print(x)

    A = []
    
    while x.shape[0] * x.shape[1] > 0 :
        
        #0deg
        try:
            A.extend(x[0,:])
            x = x[1:,:]
        except :
            break
        #90deg
        try:
            A.extend(x[:,-1])
            x = x[:,:-1]
        except :
            break
        #180deg
        try:
            A.extend(list(reversed(x[-1,:])))
            x = x[:-1,:]
        except :
            break
        #270deg
        try:
            A.extend(list(reversed(x[:,0])))
            x = x[:,1:]
        except :
            break
        
    return A    

unroll(x)

'''
unroll(x)
[[ 7  1 20 18]
 [ 0  8  3 13]
 [14 11 13 10]]
Out[116]: [7, 1, 20, 18, 13, 10, 13, 11, 14, 0, 8, 3]
'''