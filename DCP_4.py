#Good morning! Here's your coding interview problem for today.
#
#This problem was asked by Stripe.
#
#Given an array of integers, find the first missing positive integer in linear time and constant space. 
#In other words, find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
#
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
#You can modify the input array in-place.


#soln
import numpy as np

#input is a list of integers
def DPC_4(I):
    #remove non positive values
    S = sorted([i for i in I if i > 0])
    #eval space between values
    D = list(np.diff(S))
    #if no positives, return 1
    if D == []:
        return 1
    #if no space > 1, return largest number in list + 1
    elif max(D) == 1:
        y = S[-1] + 1
        return y
    #else, find the lowest val with a gap to the next val and add 1 to it.
    else:
        d = [d for d in D if d > 1][0]
        s=D.index(d)
        y=S[s]+1
        return y
    
    
#test prompt examples
I=[3, 4, -1, 1] 
DPC_4(I)
#2

I=[1, 2, 0]
DPC_4(I)
#3

#test list of only negatives
I= [-1]
DPC_4(I)
#1

#test list with duplicates
I=[1,1,3,3,4,5]
DPC_4(I)
#2

#test list with only zero
I=[0]
DPC_4(I)
#1


#soln time incl notes,comments: 25min