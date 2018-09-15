#Good morning! Here's your coding interview problem for today.
#
#This problem was asked by Jane Street.
#
#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
#Given this implementation of cons:
#
#def cons(a, b):
#    def pair(f):
#        return f(a, b)
#    return pair
#
#Implement car and cdr.

#soln
#start 10:02

#def cons per prompt
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(cons):
    #create a function that returns its inputs 
    def inr(a, b):
        return a, b
    #invoke cons on inr. this sets f = inr, and pair = inr(a, b)
    #return a
    return cons(inr)[0]


def cdr(cons):
    #create a function that returns its inputs 
    def inr(a, b):
        return a, b
    #invoke cons on inr. this sets f = inr, and pair = inr(a, b)
    #return b
    return cons(inr)[1]


#test prompt example
car(cons(3, 4))  
#3

cdr(cons(3, 4)) 
#4


#solve time incl notes,comments : 50 min
#concepts studied: types.FunctionType(cons.__code__,{}), @decorators

#notes: the challenge here was understanding how to define the functional form of f to suit the prompt, and how call it from within cons. 
#its simple to make a function that returns its inputs, but since cons takes two inputs, its at first not clear how to do it.
#once its understood that, as long as the function input to cons itself takes the same number of inputs as cons, then the problem is trivial.
