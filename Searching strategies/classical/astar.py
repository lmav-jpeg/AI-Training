'''
Implementation of the A* algorithm.
The detailed algorithm procedure and instructions are available as paid content through the Discord server.
To access the complete procedure, please purchase **Lesson 3 part 2 ** of the AI Training.
**Course:** [AI Training — Gumroad](https://lmav0242.gumroad.com/)
@author Laurie MAVOUNGOU lm9469@rit.edu lmavoungou@outlook.be
@position CEO of JK AI
'''

import math
from graph import *
from Node import *


class AStar():
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.track = {}
        self.g_tracking = {}
        self.cost = []
        self.last_neighbor = None
        self.coordinates = {start: (0, 0)}  # Initialize start coordinates
        self.f_tracking = {}
        self.best_f_tracking = {}

    def g_calculation_and_heuristics_base(self, start, goal, index=0, cost_list=None, visited=None):
        '''
        Recursive function helping to get the coordinates of the graph nodes
        and to track of the g(n) values for each node
        :param start:
        :param goal:
        :param index:
        :param cost_list:
        :param visited:
        :return:
        '''
        neighbors = self.graph.get_neighbors(start)

        if cost_list is None:
            cost_list = []

        if visited is None:
            visited = set()

        visited.add(start)
        self.g_tracking[start] = cost_list

        for i, n in enumerate(neighbors):
            if n in visited:
                continue
            self.coordinates[n] = (index + 1, i)
            cost = self.graph.get_edges_weights(start, n)
            current_cost_list = cost_list + [cost]

            # Directly track the g-cost for every visited neighbor
            self.g_tracking[n] = current_cost_list

            self.g_calculation_and_heuristics_base(
                n, goal, index + 1, current_cost_list, visited.copy()
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

    def a_star_search(self, start, goal):
        '''
        Algorithm core to find the path from start to goal.
        :param start:
        :param goal:
        :return:
        '''
        neighbors = self.graph.get_neighbors(start)
        self.f_tracking = {}
        if start == goal:
            return self.path_building(goal)
        for n in neighbors:
            if n in self.visited:
                continue
            g_value = sum(self.g_tracking[n])
            h_value = self.calculate_heuristic(n, goal)
            f_value = g_value + h_value
            self.f_tracking[n] = f_value

        self.visited.add(start)
        if not self.f_tracking:
            return None
        smallest_f=min(self.f_tracking.values())
        best_node = [key for key, val in self.f_tracking.items() if val == smallest_f][0]
        self.best_f_tracking[best_node] = smallest_f
        self.track[best_node] = start
        a_star_search_result = self.a_star_search(best_node, goal)
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
    astar = AStar(graph, start, goal)

    astar.g_calculation_and_heuristics_base(start, goal)
    path = astar.a_star_search(start, goal)
    path_strings = [str(node) for node in path]
    print(path_strings)




