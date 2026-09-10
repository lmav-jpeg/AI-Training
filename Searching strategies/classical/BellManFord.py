'''
This class represents a Bell Man-Ford algorithm using Dynamic programming
The procedure is described in the discord server as a paid content.
Buy the lesson 3 course to get access to it
Link to selling : https://lmav0242.gumroad.com/
@author: https://www.programiz.com/dsa/bellman-ford-algorithm
@author : Laurie MAVOUNGOU CEO JK AI lmavoungou@outlook.be
'''

from Node import *
from graph import *
class BellManFord:
    def __init__(self, graph:'MyGraph', start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.distances = {}
        self.track ={}


    def populating_the_table(self, start:'Node'):
        '''
        Populating the BellMan Ford table
        :param start:
        :return: None
        '''
        for node in self.graph.get_nodes():
            if node == self.start:
                self.distances[node] = 0
            else:
                self.distances[node] = float('inf')

    def bellman_ford(self, src):
        '''
        Bell Man-Ford core algorithm
        :param src:
        :return: updated distances or None
        '''
        number_of_nodes = self.graph.get_number_of_nodes()
        self.edges = self.graph.get_edges()
        self.populating_the_table(src)
        # Relax edges V-1 times
        for _ in range(number_of_nodes - 1):
            for e in self.edges:
                u = e.source; v = e.target; w = e.weight
                new_distance = min(self.distances[v], self.distances[u] + w)
                if new_distance < self.distances[v]:
                    self.distances[v] = new_distance
                    self.track[v] = u

        # Check for negative weight cycles
        for e in self.edges:
            u = e.source; v = e.target; w = e.weight
            if self.distances[u] != float('inf') and self.distances[u] + w < self.distances[v]:
                print("Graph contains a negative weight cycle")
                return None
        return self.distances

    def path_building(self):
        '''Return the path from start to goal nodes objects
        Used for Front End
        :return: list of objects nodes from start to goal.'''

        if self.goal not in self.track and self.goal != self.start:
            return []

        path = []
        predecessor = self.goal
        while predecessor != self.start:
            path.append(predecessor)
            if predecessor not in self.track:
                return [] # Safety check if path is broken
            predecessor = self.track[predecessor]
        path.append(self.start)
        path.reverse()
        return path


    def to_dict(self):
        """
        Build a dictionary representation of path from start to goal.
        :return: dictionary
        """
        dct = {}
        dct["path"] = [str(node) for node in self.path_building()]
        return dct



#Test
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

graph = MyGraph()

graph.add_edge(A, B,5)
graph.add_edge(A, C,2)
graph.add_edge(A, D,6)
graph.add_edge(B, E,8)
graph.add_edge(E, F,7)

bf= BellManFord(graph,A, F)
bf.bellman_ford(A)
print("Path:", bf.path_building())