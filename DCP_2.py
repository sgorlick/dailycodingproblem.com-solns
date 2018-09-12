#prompt:
#Good morning! Here's your coding interview problem for today.
#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

import random
import numpy as np

#for each element in a list, get the product of all other elements the list.
def DCP_2(L):
    #create container for list of products
    P = []
    #iterate through the list elements
    for i,p in enumerate(L):
        #DEBUG: test that the right indexes will be excluded from the product
        #print([j for j,q in enumerate(L) if j != i])
        #calculate the product
        P.append(np.product([q for j,q in enumerate(L) if j != i]))
    return P

#save products to a list :
    
#test example lists:
#1:
L = [3, 2, 1]
D = DCP_2(L)
print(D)

#2:
L = [1, 2, 3, 4, 5]
D = DCP_2(L)
print(D)

#test a random list of ints of user-specified len n:
n = 10 
L = [ random.randint(1,10) for x in range(n) ]
D = DCP_2(L)
print(D)


#NOTE: follow-up irrelevant, division not used in sol'n (numpy was allowed, right? :) )