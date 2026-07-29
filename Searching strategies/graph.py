'''
This class is the base of all search strategies.
It contains the functions enabling the creation
of a graph

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''
class MyGraph:
    def __init__(self):
        self.nodes = {}
        self.count = 0
        self.edges = {}

    def add_node(self, node:'Node'):
        if node not in self.nodes:
            self.nodes[node] = []
            print("Node added")
            self.count += 1
        else:
            print("Node already added")

    def add_edge(self, node1:'Node', node2:'Node', weight:int =0):
        "Case of undirected graph"
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        if node2 not in self.nodes[node1]:
            self.nodes[node1].append(node2)
        if node1 not in self.nodes[node2]:
            self.nodes[node2].append(node1)
        self.edges[(node1, node2)] = weight
        self.edges[(node2, node1)] = weight

    def contains(self, node:'Node'):
         return node in self.nodes.keys()

    def get_neighbors(self, node:'Node'):
        return self.nodes[node]






