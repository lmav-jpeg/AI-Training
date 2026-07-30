'''
This code implement the recursive DFS algorithm.
Keeping track of all nodes visited.
And storing the last node visited to rebuild the path

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''
from Node import *
from graph import *

class DFS:
    def __init__(self, start:'Node', goal:'Node', graph:'MyGraph'):
        '''
        Constructor.
        :param start:
        :param goal:
        :param graph:
        '''
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.track = {}
        self.last_neighbor = None

    def DFS(self, start):
        '''
        Traversal of the DFS algorithm.
        :param start:
        :return: None
        '''
        if start not in self.visited:
            self.visited.add(start)
        begin_neighbors = self.graph.get_neighbors(start)
        if begin_neighbors:
            for neighbor in begin_neighbors:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    if neighbor == self.goal:
                        self.last_neighbor = start
                        break
                    self.track[neighbor] = start
                    self.DFS(neighbor)

    def path_building(self):
        '''
        Building a path backward from goal to start.
        :return: str
        '''
        path = str(self.last_neighbor) + ' -> ' + str(self.goal)
        predecessor = self.last_neighbor
        while predecessor != self.start:
            predecessor = self.track[predecessor]
            path = str(predecessor) + ' -> ' + path
        return path



'''
Test case
'''

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

graph = MyGraph()

graph.add_edge(A, B)
graph.add_edge(A, C)
graph.add_edge(A, D)
graph.add_edge(B, E)
graph.add_edge(E, F)

print("A's neighbors:", [str(node) for node in graph.get_neighbors(A)])

dfs = DFS(A, F, graph)

dfs.DFS(A)
print("Path:", dfs.path_building())