'''
Implementation of the iterative algorithm DIJKSTRA.
Using a built-in function priotity queue

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

from Node import *
from graph import *
from queue import PriorityQueue

class DIJKSTRA:
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
        self.queue = PriorityQueue()
        self.distances = {}

    def populating_the_table(self, start:'Node'):
        '''
        Populating the DIJSKTRA table
        :param start:
        :return: None
        '''
        for node in self.graph.get_nodes():
            if node is start:
                self.distances[start] = 0
            else:
                self.distances[node] = float('inf')


    def DKSTR(self, start):
        '''
        Core of the Dijkstra algorithm
        :param start:
        :return: None
        '''
        self.queue.put((0,start))
        distance = self.distances[start]
        begin_neighbors = self.graph.get_neighbors(start)
        for neighbor in begin_neighbors:
            weight = self.graph.get_edges_weights(neighbor, start)
            new_distance = distance + weight
            if new_distance < self.distances[neighbor]:
                self.distances[neighbor] = new_distance
                self.queue.put((new_distance,neighbor))
                self.track[neighbor] = start

        while not self.queue.empty():
            distance, current = self.queue.get(timeout=1)
            if current == self.goal:
                self.last_neighbor = current
                break
            ongoing_neighbors = self.graph.get_neighbors(current)
            for neighbor1 in ongoing_neighbors:
                weight = self.graph.get_edges_weights(neighbor1, current)
                new_distance = distance + weight
                if new_distance < self.distances[neighbor1]:
                    self.queue.put((new_distance, neighbor1))
                    self.distances[neighbor1] = new_distance
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

graph.add_edge(A, B,5)
graph.add_edge(A, C,2)
graph.add_edge(A, D,6)
graph.add_edge(B, E,8)
graph.add_edge(E, F,7)

print("A's neighbors:", [str(node) for node in graph.get_neighbors(A)])

dijkstra = DIJKSTRA(A, F, graph)
dijkstra.populating_the_table(A)
dijkstra.DKSTR(A)
print("Path:", dijkstra.path_building())