'''
This class is the base of all search strategies.
It contains the functions enabling the creation of a vertices
of a graph

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoung@outlook.be
@position CEO of JK AI
'''
class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)