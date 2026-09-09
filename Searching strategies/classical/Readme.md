# 🌐 Graphical Representation

This project provides a **graphical representation** of the implemented graph-search algorithms using a web-based frontend.

The visualization allows you to interact with and compare:

* 🔵 **BFS** — Breadth-First Search
* 🟣 **DFS** — Depth-First Search
* 🟢 **Dijkstra** — Shortest-Path Algorithm

---

## 🚀 How to Run

### 1️⃣ Start the Retriever

Open a terminal in the project directory and run:

```bash
python retriever.py
```

The Flask backend will start and make the graphical interface available.

---

### 2️⃣ Open Your Browser 🌍

Open your preferred web browser and visit:

```text
http://127.0.0.1:5000
```

Alternatively:

```text
http://localhost:5000
```

---

## 🖥️ Using the Graphical Interface

Once the page is open, you will see the graph visualization and the algorithm buttons.

### 🔵 BFS

Click the **BFS** button to run Breadth-First Search.

The resulting path will be displayed below the graph and highlighted visually.

### 🟣 DFS

Click the **DFS** button to run Depth-First Search.

The graph will update and highlight the path found by DFS.

### 🟢 Dijkstra

Click the **Dijkstra** button to run Dijkstra's shortest-path algorithm.

The weighted edges are displayed in the graph, and the shortest path is highlighted.

---

## 🎨 Visualization

The frontend uses colors to make the result easier to understand:

| Element             | Representation                          |
| ------------------- | --------------------------------------- |
| 🟢 Normal node      | Node that is not part of the final path |
| 🔵 Path node        | Node belonging to the resulting path    |
| ⚪ Normal edge       | Regular graph connection                |
| 🔵 Highlighted edge | Edge belonging to the resulting path    |
| 🔢 Edge weight      | Weight associated with an edge          |

The selected algorithm's path is also displayed as text below the graph.

Example:

```text
BFS Path: A → B → E → F
```

---

## 🔄 Run Another Algorithm

You can switch between algorithms at any time.

Simply click another button:

```text
🔵 BFS     🟣 DFS     🟢 Dijkstra
```

The graph visualization will automatically update with the result of the selected algorithm.

---

## 🛠️ Troubleshooting

If the graphical representation does not appear:

### ✅ Check that the backend is running

Make sure you started:

```bash
python retriever.py
```

### ✅ Check the browser address

Make sure you are accessing:

```text
http://127.0.0.1:5000
```

### ✅ Check the terminal

If something goes wrong, check the terminal where `retriever.py` is running for error messages.

---

## 📌 Quick Start

For a quick launch:

```bash
python retriever.py
```

Then open:

```text
http://127.0.0.1:5000
```

🎯 **Select BFS, DFS, or Dijkstra and explore the graphical representation of the algorithms!**
