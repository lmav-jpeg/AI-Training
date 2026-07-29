'''
Implementation of the iterative algorithm of DFS.
Using a stack

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

from Node import *
from graph import *
from collections import deque

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
        self.stack = deque()

    def DFS(self, start):
        if start not in self.visited:
            self.visited.add(start)
        begin_neighbors = self.graph.get_neighbors(start)
        for neighbor in begin_neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.stack.append(neighbor)
                self.track[neighbor] = start

        while self.stack:
            current = self.stack.pop()
            if current == self.goal:
                self.last_neighbor = current
                break
            ongoing_neighbors = self.graph.get_neighbors(current)
            for neighbor1 in ongoing_neighbors:
                if neighbor1 not in self.visited:
                    self.visited.add(neighbor1)
                    self.stack.append(neighbor1)
                    self.track[neighbor1] = current


    def path_building(self):
        '''
        Building a path backward from goal to start.
        :return: string representing the path from start to goal.
        '''
        path = str(self.last_neighbor)
        predecessor = self.last_neighbor
        while predecessor != self.start:
            predecessor = self.track[predecessor]
            path = str(predecessor) + ' -> ' + path
        return path



#Test
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