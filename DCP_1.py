import itertools
import random


def DCP_1(n,k=k):
    L = [ random.randint(1,100) for x in range(n) ]
    print('is '+str(k)+' the sum of any two elements of '+str(L))
    return sum([I[0]+I[1]==k for I in list(itertools.permutations(L,2))]) > 0
    
#set search list size (randomly generated ints between 1 and 100)
n=10
#set goal number k
k = random.randint(1,100)
#test whether  k is a sum of any pair in list
DCP_1(n,k)