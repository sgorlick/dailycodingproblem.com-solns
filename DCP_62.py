# -*- coding: utf-8 -*-
"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

from scipy.special import comb

def f(m,n):        
    k=min(m-1,n-1) #since matrix is transposable, can also use max w/ same result.
    n=(m-1)+(n-1)
    print(comb(n,k))


#test:

f(2,2)
#2
f(5,5)
#70


#test transposition
f(10,4)
#220

f(4,10)
#220

#solve time : 5 minutes