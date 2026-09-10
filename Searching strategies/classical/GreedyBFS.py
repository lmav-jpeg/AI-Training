'''
Implementation of the Greedy BFS algorithm.
The procedure is described in:
    https://github.com/lmav-jpeg/AI-Training/blob/main/Searching%20strategies/classical/gbfs_walkthrough.md

@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

import math
from graph import *
from Node import *


class GBFS():
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.track = {}
        self.last_neighbor = None
        self.coordinates = {start: (0, 0)}  # Initialize start coordinates
        self.h_tracking = {}
        self.best_h_tracking = {}

    def heuristics_base(self, start, goal, index=0, visited=None):
        '''
        Recursive function helping to get the coordinates of the graph nodes
        :param start:Node
        :param goal:Node
        :param index:int
        :param visited:set
        :return:
        '''
        neighbors = self.graph.get_neighbors(start)

        if visited is None:
            visited = set()

        visited.add(start)

        for i, n in enumerate(neighbors):
            if n in visited:
                continue
            self.coordinates[n] = (index + 1, i)
            self.heuristics_base(
                n, goal, index + 1, visited.copy()
            )
        return



    def calculate_heuristic(self, node, goal, predecessors=None):
        '''
        Euclidean distance between a node and a goal node
        :param node:
        :param goal:
        :param predecessors:
        :return:
        '''
        x1, y1 = self.coordinates[node]
        x2, y2 = self.coordinates[goal]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def gbfs_search(self, start, goal):
        '''
        Algorithm core to find the path from start to goal.
        :param start:
        :param goal:
        :return:
        '''
        neighbors = self.graph.get_neighbors(start)
        if start == goal:
            return self.path_building(goal)
        for n in neighbors:
            if n in self.visited:
                continue

            if n not in self.h_tracking:
                h_value = self.calculate_heuristic(n, goal)
                self.h_tracking[n] = h_value
                self.track[n] = start

        self.visited.add(start)
        if not self.h_tracking:
            return None
        smallest_f=min(self.h_tracking.values())
        best_node = [key for key, val in self.h_tracking.items() if val == smallest_f][0]
        self.best_h_tracking[best_node] = smallest_f
        self.track[best_node] = start
        # Remove the selected node from the candidates
        del self.h_tracking[best_node]
        a_star_search_result = self.gbfs_search(best_node, goal)
        return a_star_search_result

    def path_building(self, goal):
        '''Return the path from start to goal nodes objects
                Used for Front End
                :return: list of objects nodes from start to goal.'''
        path = [goal]
        current = goal
        while current in self.track:
            current = self.track[current]
            path.append(current)
        path.reverse()
        return path

    def to_dict(self):
        """
        Build a dictionary representation of path from start to goal.
        :return: dictionary
        """
        dct = {}
        dct["path"] = [str(node) for node in self.path_building(self.goal)]
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
    gbfs = GBFS(graph, start, goal)

    gbfs.heuristics_base(start, goal)
    path = gbfs.gbfs_search(start, goal)
    path_strings = [str(node) for node in path]
    print(path_strings)




