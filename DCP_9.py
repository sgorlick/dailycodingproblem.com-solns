#prompt:
#Good morning! Here's your coding interview problem for today.
#This problem was asked by Airbnb.
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#Follow-up: Can you do this in O(N) time and constant space?


#sol'n
from itertools import permutations
from numpy.random import randint
from math import ceil


#list of values
x = [4, 5, 6, 7, 8]


#simple version:
def f(x):
prev, total = 0, 0

for i in x:
    print(prev,prev+i,total)
    prev, total = total, max(total, prev + i)
    print(prev,total)
return total

f(x)


#version that lets you know which indeces the values belong to
##sample the adjacency evaluation method:

#list indexes
x_idx = [n for n in range(len(x))]
#list length
len_x = len(x)
#test all permutations of 3 indexes (could be any number between 1 and len_x)
i = list(permutations(x_idx,3))[0]
#evaluate all pairs of indexes in those permutations
I = list(permutations(i,2))
#evaluate whether the indexes are adjacent for any pair
[abs( list(permutations(i,2))[j][0] -list(permutations(i,2))[j][1] ) > 1 for j in range(len(list(permutations(i,2)))) ]  
#evaluate whether the indexes are adjacent for ALL pairs
all([abs( list(permutations(i,2))[j][0] -list(permutations(i,2))[j][1] ) > 1 for j in range(len(list(permutations(i,2)))) ]  ) 
#print a list of non-adjacent indexes: 
[i for i in list(permutations(x_idx,3)) if all([abs( list(permutations(i,2))[j][0] -list(permutations(i,2))[j][1] ) > 1 for j in range(len(list(permutations(i,2)))) ]  ) ]

#output function:
def DCP_9(x):
    x_idx = [n for n in range(len(x))]
    len_x = len(x) 
    K = []
    #iterate over ceil(len_x/2). this is the maximum number of non-adjacent values by the pidgeonhole principle
    for n in range(ceil(len_x/2)):
        K.extend([ i for i in list(permutations(x_idx,n+1)) if all([abs( list(permutations(i,2))[j][0] - list(permutations(i,2))[j][1] ) > 1 for j in range(len(list(permutations(i,2)))) ]  ) ])
    #identify the max sum of non-adjacent elements
    S = max([sum([x[n] for n in k]) for k in K])
    #list the indexes that are used in S
    #Z = [k for k in K if sum([x[n] for n in k]) == max([sum([x[n] for n in k]) for k in K])]
    return S#,Z


#test prompt values
x = [2, 4, 6, 2, 5] 
print(DCP_9(x))
#13

x = [5, 1, 1, 5]
print(DCP_9(x))
#10

#test negative and zero values:
x = [-4, 1, 1, 0]
print(DCP_9(x))

#test random values
x = randint(-200,200,size=11)
print(DCP_9(x))








mem = None

x = [2, 4, 6, 2, 5] 




0,0
2> 0,max(0,0+2)=2
4> 2,max(2,2+4)=6















x = randint(-200,200,size=20)



x = [1,1,9,10,9,]