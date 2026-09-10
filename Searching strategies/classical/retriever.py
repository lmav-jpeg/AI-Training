from flask import Flask, render_template, jsonify
from graph import  *
from Node import *
from BFS import *
from DFS import *
from Dijkstra import *
from astar import *

app = Flask(__name__)

# 1. Create your graph
my_graph = MyGraph()

# 2. Add your nodes and edges using your methods
#Test
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")


my_graph.add_node(node_a)
my_graph.add_node(node_b)
my_graph.add_node(node_c)
my_graph.add_node(node_d)
my_graph.add_node(node_e)
my_graph.add_node(node_f)
my_graph.add_edge(node_a, node_b, status="up")
my_graph.add_edge(node_a, node_c, status="up")
my_graph.add_edge(node_a, node_d, status="up")
my_graph.add_edge(node_e, node_f, status="up")
my_graph.add_edge(node_b, node_e, status="up")

#Test
node_g = Node("G")
node_h = Node("H")
node_i = Node("I")
node_j = Node("J")
node_k = Node("K")
node_l = Node("L")


graph2 = MyGraph()

graph2.add_edge(node_g, node_h,5)
graph2.add_edge(node_g, node_i,2)
graph2.add_edge(node_g, node_j,6)
graph2.add_edge(node_h, node_k,8)
graph2.add_edge(node_k, node_l,7)

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

graph1 = MyGraph()
start = A
goal = F
graph1.add_edge(A, B, 2)
graph1.add_edge(A, C, 4)
graph1.add_edge(A, D, 7)
graph1.add_edge(B, E, 3)
graph1.add_edge(C, E, 1)
graph1.add_edge(D, F, 2)
graph1.add_edge(E, F, 2)


@app.route("/")
def index():
    return render_template("index.html")
# 3. Then your API route serves that populated graph
# -------------------------
# GRAPH + BFS
# -------------------------
@app.route("/api/bfs", methods=["GET"])
def get_graph():
    bfs = BFS(node_a, node_f, my_graph)
    bfs.BFS(node_a)
    graph_data = my_graph.to_dict()
    bfs_data = bfs.to_dict()
    graph_data.update(bfs_data)
    return jsonify(graph_data)

# -------------------------
# GRAPH + DFS
# -------------------------
@app.route("/api/dfs", methods=["GET"])
def get_graph2():
    dfs = DFS(node_a, node_f, my_graph)
    dfs.DFS(node_a)
    graph_data = my_graph.to_dict()
    dfs_data = dfs.to_dict()
    graph_data.update(dfs_data)
    return jsonify(graph_data)

# -------------------------
# GRAPH + DIJKSTRA
# -------------------------
@app.route("/api/dijkstra", methods=["GET"])
def get_graph3():
    dijkstra = DIJKSTRA(node_g, node_l, graph2)
    dijkstra.populating_the_table(node_g)
    dijkstra.DKSTR(node_g)
    graph_data2 = graph2.to_dict()
    dijkstra_data = dijkstra.to_dict()
    graph_data2.update(dijkstra_data)
    return jsonify(graph_data2)

# -------------------------
# GRAPH + A*
# -------------------------
@app.route("/api/astar", methods=["GET"])
def get_graph4():
    astar = AStar(graph1, start, goal)
    astar.g_calculation_and_heuristics_base(start, goal)
    astar.a_star_search(start, goal)
    graph_data3 = graph1.to_dict()
    astar_data = astar.to_dict()
    graph_data3.update(astar_data)
    return jsonify(graph_data3)

if __name__ == "__main__":
    app.run(debug=True)