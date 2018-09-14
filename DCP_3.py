#Good morning! Here's your coding interview problem for today.
#
#This problem was asked by Google.
#
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
#For example, given the following Node class

#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
        
#The following test should pass:

#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'



#soln (use pickle)
import pickle

#define test class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#define serialize (as pickle.dumps)
def serialize(a):
    return pickle.dumps(a)

#define serialize (as pickle.loads)
def deserialize(a):
    return pickle.loads(a)   


class soln:
    def __init__(self, node):
        self.node = node
    
    def proof(self):
       assert deserialize(serialize(node)).left.left.val == 'left.left' 
       return deserialize(serialize(node)).left.left.val == 'left.left' 

#set example node
node = Node('root', Node('left', Node('left.left')), Node('right'))       
     
#test proof 
soln.proof(node)

















class Animal:
   def __init__(self, number_of_paws, color):
       self.number_of_paws = number_of_paws
       self.color = color

class Sheep(Animal):
   def __init__(self, color):
       Animal.__init__(self, 4, color)

mary = Sheep("white")

print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))

my_pickled_mary = pickle.dumps(mary)

print ("Would you like to see her pickled? Here she is!")

print (my_pickled_mary)

dolly = pickle.loads(my_pickled_mary)



print (dolly)

print (str.format("My sheep mary is {0} and has {1} paws", dolly.color, dolly.number_of_paws))


