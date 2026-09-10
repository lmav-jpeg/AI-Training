'''
Implementation of Iterative DDFS.
This implementation is based on the GeekForGeeks implementation in python.
We only added the path building.
@author Neelam Pandey GeeksForGeeks
@author Laurie MAVOUNGOU  CEO JK AI lm9469@rit.edu
'''

from graph import *
from Node import *
class IDDFS():
    def __init__(self, graph:'MyGraph', start:'Node', goal:'Node'):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.track = []
        self.adjacency = self.graph.get_adjacency_list()
        self.last_neighbor = None

    def DepthLimitedSearch(self, start, goal, tracker, DepthLimit=50):
        '''
        Looks all node in depth until we reach the goal.
        A depth limit of 50 is the maximum depth.
        :param start:
        :param goal:
        :param tracker:
        :param DepthLimit:
        :return:
        '''
        if start == goal:
            tracker.append(start)
            self.track = tracker.copy()
            return tracker
        if tracker is None:
            tracker = []
        if DepthLimit <= 0:
            return None

        tracker.append(start)

        for i in self.adjacency[start]:
            if i not in tracker:
                result = self.DepthLimitedSearch(i,goal,tracker.copy(),DepthLimit - 1)

                if result is not None:
                    return result

        return None

    def IDDFS(self, src, target, maxDepth):
        # Repeatedly depth-limit search till the
        # maximum depth
        tracker = []
        for i in range(maxDepth):
            if (self.DepthLimitedSearch(src, target,tracker, i)):
                return True
        return False

    def to_dict(self):
        """
        Build a dictionary representation of path from start to goal.
        :return: dictionary
        """
        dct = {}
        dct["path"] = list(dict.fromkeys(str(node) for node in self.track))
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

source=A; target = F; maxDepth = 10; src = A

instance = IDDFS(graph,source, target)
if instance.IDDFS(src, target, maxDepth) == True:
    print ("Target is reachable from source " +
        "within max depth")
    print(list(dict.fromkeys(str(node) for node in instance.track)))
else :
    print ("Target is NOT reachable from source " +
        "within max depth")