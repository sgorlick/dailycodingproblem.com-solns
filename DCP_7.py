


from itertools import permutations
import numpy as np

x = 111



    
#convert x to string for position indexing
x_str = str(x)

#separate digits of x
X = []
for i in range(len(x_str)):
    X.append(int(x_str[i]))

P = []        
#evaluate all 1&2 digit combinations of positions of x
for i in range( len(str(x))//2):
    P.append(2)
if len(str(x))%2 == 1:
    P.append(len(str(x))%2)
#generate all orderings with set permutations
P = list(set(permutations(P,len(P))))
P.append(X)

#evaluate whether the positions are decodable (ie: the digits sum to no more than the number of letters in the alphabet (26))
QQ = []
#iterate over all permutations of the product
for p in P: 
    j = 0
    Q = [] 
    i = 0
    #iterate over all per
    while j < len(x_str):
        #grab the digits of x assoc. with the current eval
        q = int(x_str[j:sum(p[:i+1])])
        #test whether the digits sum to no more than the number of letters in the alphabet (26)
        if q < 27 :
            Q.append(q)
            j = sum(p[:i+1])
            i = i + 1
        else:
            #print('not decodable')
            break
    if len(Q) == len(p):
        QQ.append(Q)


characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


A = []
for G in QQ:
    B = str()
    for g in G:
        B = B + characters[g-1]
    A.append(B)

    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        x_str = str(x)
        

        
        
        P = []
        for i in range( len(str(x))//2):
            P.append(2)
        if len(str(x))%2 == 1:
            P.append(len(str(x))%2)
        P = list(set(permutations(P,len(P))))
        
        #
        QQ = []
        for p in P: 
            j = 0
            Q = [] 
            i = 0
            while j < len(x_str):
                q = int(x_str[j:sum(p[:i+1])])
                if q < 27 :
                    Q.append(q)
                    j = sum(p[:i+1])
                    i = i + 1
                else:
                    print('not decodable')
                    break
            if len(Q) == len(p):
                QQ.append(Q)
        
        
        characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        
        A = []
        for P in QQ:
            B = str()
            for p in P:
                B = B + characters[p-1]
            A.append(B)
            



























##V1
p = P[1]
j=0

Q = int(x_str[j:sum(p[:1])])
j = sum(p[:1])

Q = int(x_str[j:sum(p[:2])])
j = sum(p[:2])

Q = int(x_str[j:sum(p[:3])])
j = sum(p[:3]) 





itertools.


list(permutations(X,2))

len(str(x))//1

len(str(x))//2

if len(str(x)) == 1:
    return [1]
if len(str(x))//2 == 1:
    return [1,2],len(str(x))//2



(1,1,1)
(1,11)
(11,1)




