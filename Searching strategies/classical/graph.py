'''
This class is the base of all search strategies.
It contains the functions enabling the creation
of a graph

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

from Edge import *

class MyGraph:
    def __init__(self):
        self.nodes = {}
        self.count = 0
        self.edges = {}
        self.adjacency_list = {}
        self.edges_track = []

    def add_node(self, node:'Node'):
        if node not in self.nodes:
            self.nodes[node] = []
            self.adjacency_list[node] = []
            print("Node added")
            self.count += 1
        else:
            print("Node already added")

    def add_edge(self, node1:'Node', node2:'Node', weight:int =0, status:str = "up"):
        "Case of undirected graph"
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        if node2 not in self.nodes[node1]:
            self.nodes[node1].append(node2)
        if node1 not in self.nodes[node2]:
            self.nodes[node2].append(node1)
        self.adjacency_list[node1].append(node2)
        self.edges[(node1, node2)] = weight
        self.edges[(node2, node1)] = weight
        color= "#2ecc71" if status == "up" else "#ff4d4d"
        edge = Edge(node1, node2, weight, status, color)
        self.edges_track.append(edge)

    def get_adjacency_list(self):
        return self.adjacency_list
    def contains(self, node:'Node'):
         return node in self.nodes.keys()

    def get_neighbors(self, node:'Node'):
        return self.nodes[node]

    def get_edges_weights(self, node1:'Node', node2:'Node'):
        return self.edges[(node1, node2)]

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges_track

    def to_dict(self):
        # Convert whatever your internal structure is
        # into the simple format the frontend expects
        return {
            "nodes": [{"id": str(node), "label": str(node)} for node in self.nodes.keys()],
            "edges": [{"from": str(e.source), "to": str(e.target),"weight":e.weight,"color": e.color, "status": e.status} for e in self.get_edges()]
        }






