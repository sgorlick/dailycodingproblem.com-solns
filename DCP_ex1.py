#prompt:
#There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
#For example, if N is 4, then there are 5 unique ways:
#
#1, 1, 1, 1
#2, 1, 1
#1, 2, 1
#1, 1, 2
#2, 2
#What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.


#sol'n:

import itertools

#input a staircase length(N) and list of step sizes(s). assumes s is de-duplicated.
def DCP_ex1(N,s):
    #save list of step orders in NN
    NN = []  
    #iterate over each possible total step count
    for n in range(N):
        #for each step count, evaluate all combinations of step sizes
        for I in itertools.combinations_with_replacement(s,n+1) :
            #identify combinations of step sizes equal to the staircase length
            if sum(I) == N:
                #evaluate all orderings of valid step combinations and save them to NN (using set to remove equivalent orderings) 
                for x in set(itertools.permutations(I)) :
                    NN.append(x)
    #return the number of unique stair climbing ways (and return the ways themselves for debugging)
    return len(NN),sorted(NN,key=len,reverse=True)
      
#test with prompt values
N=4
s=(1,2)
DCP_ex1(N,s)
#(5, [(1, 1, 1, 1), (1, 2, 1), (2, 1, 1), (1, 1, 2), (2, 2)])

N=4
X=(1,3,5)
DCP_ex1(N,X)
#(3, [(1, 1, 1, 1), (1, 3), (3, 1)])



#sol'n time (incl notes, comments, testing): 25 min

#NOTE that for small values of N (4, 6, ...) the function is very fast, returing in less than 1 second.
#when i tried this for N=29, the function computed for over 5 minutes before I halted it.