# 🎯 Greedy Best-First Search (GBFS) Algorithm Walkthrough

> *"GBFS is using an estimation of how much it will cost to reach the goal ($h$), and it uses that to decide which node to explore next."* 🧭✨

---

## 💡 The Core Variable

- **`h(n)`** = 🎯 The estimated cost (Euclidean distance) from node $n$ to the goal

---

## 🗺️ Setup & Initialization

So I should have a dictionary that keeps track of each node and coordinates associated to each node. 🗂️📍

I start with:
- **`A = (0,0)`** 🚩

---

## 🔍 Exploring Neighbors from A

Then I move to the reachable nodes from A: 🔍
- `A → B` ➡️
- `A → C` ➡️
- `A → D` ➡️

For each reachable node, I have their coordinates. I look at the traversal information and calculate the Euclidean distance from that node to the goal. I will have a traversal/heuristic function for that. 📏🧠

So I update:
- `h(B) = estimated cost from B to the goal`
- `h(C) = estimated cost from C to the goal`
- `h(D) = estimated cost from D to the goal`

---

## ⭐ Choosing the Best Node & Iterative Loop

- Then I choose the node with the smallest `h(n)`. ⭐
- That node becomes my current node, and I move to its reachable neighbors. 🏃‍♂️💨

For each new neighbor, I calculate the estimated cost to the goal:
- `h(node) = Euclidean distance(node, goal)`

I do the same process again and choose the node with the smallest `h(n)`. 🔄

I continue doing this until I reach the goal. 🏁

---

## 🔗 Tracking Paths & Re-visiting Nodes

At the same time, I need to keep track of the predecessor of each node so that, once I reach the goal, I can reconstruct the path that was found. 🧵🗺️

One important thing is that if I reach a node that I have already visited, I should compare its `h(n)` with the current neighbor `h(n)`. If the new path has a lower cost, I update the cost and the predecessor. 🔄💡
