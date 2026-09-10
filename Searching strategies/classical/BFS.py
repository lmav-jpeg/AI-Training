'''
Implementation of the iterative algorithm Breadth-First Search BFS.
Using a built-in function queue

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

from Node import *
from graph import *
from queue import Queue

class BFS:
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
        self.queue = Queue()

    def BFS(self, start):
        if start not in self.visited:
            self.visited.add(start)
        begin_neighbors = self.graph.get_neighbors(start)
        for neighbor in begin_neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.queue.put(neighbor)
                self.track[neighbor] = start

        while not self.queue.empty():
            current = self.queue.get(timeout=1)
            if current == self.goal:
                self.last_neighbor = current
                break
            ongoing_neighbors = self.graph.get_neighbors(current)
            for neighbor1 in ongoing_neighbors:
                if neighbor1 not in self.visited:
                    self.visited.add(neighbor1)
                    self.queue.put(neighbor1)
                    self.track[neighbor1] = current
        return self.path_building2()


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

    def path_building2(self):
        '''Return the path from start to goal nodes objects
        Used for Front End
        :return: list of objects nodes from start to goal.'''

        if self.last_neighbor is None:
            return []

        path = []

        predecessor = self.last_neighbor

        while predecessor != self.start:
            path.append(predecessor)
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
        dct["path"] = [str(node) for node in self.path_building2()]
        return dct




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

bfs = BFS(A, F, graph)

bfs.BFS(A)
print("Path:", bfs.path_building())
