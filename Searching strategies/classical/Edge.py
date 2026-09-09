"""
This class serve as base for the front end graph representation
It is the computational representation of an edge

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
"""
class Edge:
    def __init__(self, source, target, weight, color, status="up", ):
        self.source = source
        self.target = target
        self.weight = weight
        self.status = status # "up" or "down"
        self.color=color