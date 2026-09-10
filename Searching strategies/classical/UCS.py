'''
Implementation of the UCS algorithm.
The procedure is described in:
    https://github.com/lmav-jpeg/AI-Training/blob/main/Searching%20strategies/classical/ucs_algorithm_logic.md

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

import math
from graph import *
from Node import *
from heapq import *
from itertools import *

class UCS():
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.track = {}
        self.goal = goal
        self.start = start

    def uniform_cost_search(self, start: 'Node', goal: 'Node'):
        '''
        The heap here is represented as a list
        the Heapq class help to perform the selection of the node with
        the smallest cost
        Count is used here to tie_break between nodes of same cost to perform FIFO
        :param start:
        :param goal:
        :return:
        '''
        counter = count()  # Unique tie-breaker counter

        pq = [(0, next(counter), start, [start])]
        visited = set()

        while pq:
            cumulative_cost, _, current, path = heappop(pq)
            self.track[current] = path
            if current == goal:
                return cumulative_cost, path
            if current in visited:
                continue

            visited.add(current)
            neighbors = self.graph.get_neighbors(current)

            for n in neighbors:
                if n not in visited:
                    edge_cost = self.graph.get_edges_weights(current, n)
                    total_cost = cumulative_cost + edge_cost
                    heappush(pq, (total_cost, next(counter), n, path + [n]))

        return None

    def path_building(self, goal):
        '''Return the path from start to goal nodes objects
        Used for Front End
        :return: list of objects nodes from start to goal.'''
        return self.track.get(goal, [])

    def to_dict(self):
        """
        Build a dictionary representation of path from start to goal.
        :return: dictionary
        """
        dct = {}
        path = self.path_building(self.goal)
        dct["path"] = [str(node) for node in path]
        return dct


if __name__ == '__main__':
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")

    graph = MyGraph()
    start = A
    goal = F
    graph.add_edge(A, B, 2)
    graph.add_edge(A, C, 4)
    graph.add_edge(A, D, 7)
    graph.add_edge(B, E, 3)
    graph.add_edge(C, E, 1)
    graph.add_edge(D, F, 2)
    graph.add_edge(E, F, 2)
    ucs = UCS(graph, start, goal)

    ucs.uniform_cost_search(start, goal)
    path = ucs.path_building(goal)
    path_strings = [str(node) for node in path]
    print(path_strings)




