class Graph:
    def __init__(self):
        self.nodes = {}
        self.count = 0

    def add_node(self, node:'Node'):
        if node not in self.nodes:
            self.nodes[node] = []
            print("Node added")
            self.count += 1
        else:
            print("Node already added")

    def add_edge(self, node1:'Node', node2:'Node', weight:int =0):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)
        self.weights = weight

    def contains(self, node:'Node'):
         return node in self.nodes.keys()





