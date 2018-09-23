#This problem was asked by Amazon.

#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

#For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def DCP_13(s,k):
    #ciel k by the number of unique characters in the string.
    k = min(len(set(s)),k)
    #handle simply maximal/minimal trivial cases:
    if len(set(s)) == k:
        print(len(s))
    elif k == 1:
        print(1)
    #handle all other cases
    else:
        #store longest string in out
        out=str()
        #iterate overall positions of the string
        for j in range(len(s)):
            #set position of first character in current run
            i=0
            #reset reviewed substring for current run
            left=str()
            #get the longest consecutive substring of k unique characters, starting at position i
            #limit loop count to length of s -- this could be shortened to the # of yet unevaluated charactersthis run to speed execution time on long strings
            while len(set(left)) <= k and i <= len(s) 
                left=s[j:i+1]
                i=i+1
            #test whether the current run is the longest so far, if so save it as the best candidate.
            if len(out) < len(left[:-1]):
                out = left[:-1]
        #print the length of the best candidate
        print(len(out))

#test example from prompt
s = "abcba"
k = 2
DCP_13(s,k)
#3

#test where k = total number of elements in s
s = "abcba"
k = 3
DCP_13(s,k)
#5

#test where k > total number of elements in s
s = "abcba"
k = 4
DCP_13(s,k)
#5

#test repeated values
s = "bbcba"
k = 2
DCP_13(s,k)
#4

    
#test longer strings
s = 'find the length of the longest substring that contains at most k distinct characters'
k = 5
DCP_13(s,k)
#8


#test karger values of k
s = 'Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.'
k = 16
DCP_13(s,k)
#64


#solve time : 1h50m incl notes,comments
#the main challenges here were making the function robust to repeated elements. 
#i tried to implement dynamic programming to speed up excecution time.









##beta soln's, complex and dont handle special cases (repeated digits, etc.)
#def DCP_13(s,k):
#    #trivial if k=1
#    if k == 1:
#        print(1)
#    else:
#        #count rightmost digit index added to sol'n
#        i=0
#        #count leftmost digit index saved to sol'n
#        j=0
#        #starting sol'n w at the beginning of the string
#        left=s[i:k+i]
#        #save sol'n value
#        out=str()
#        #iterate over all sections of the string
#        while i+k < len(s):
#            i=i+1
#            #store the next possible starting point w/ k-elements
#            right=s[j:k+i]
#            if len(set(right)) > k :
#                j=j+1
#                right=s[j:k+i]
#            #test whether the adjacent starting points have the same elements
#            if set(left).issubset( set(right) ) :#set(left) == set(right):
#                left=s[j:k+i]
#                out=left
#            else:
#                left=s[i:k+i]
#                j=j+1
#        print(len(out))
#finish:10:58


#
#def DCP_13(s,k):
#    i=0
#    j=0
#    left=str()
#    out=str()
#    while j+1 != i :
#        while len(set(left)) <= k:
#            left=s[j:i+1]
#            i=i+1
#        out = left[:-1]
#        j=j+len(out)
#        left=str()
#    return print(len(out))



