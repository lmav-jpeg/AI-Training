# 🚀 A* Algorithm Walkthrough

> *"A* is using the cost I already paid to get somewhere ($g$) + an estimation of how much it will cost to reach the goal ($h$), and it uses that to decide which node to explore next."* 🧭✨

---

## 💡 The Core Variables

- **`g(n)`** = 🛤️ The cost already traveled from the start to $n$
- **`h(n)`** = 🎯 The estimated cost from $n$ to the goal
- **`f(n)`** = 📊 The estimated total cost

---

## 🗺️ Setup & Initialization

So I should have a dictionary that keeps track of each node and the traversal possibilities between nodes with their costs. 🗂️

I start with:
- **`g(A) = 0`** 🚩

---

## 🔍 Exploring Neighbors from A

Then I move to the reachable nodes from A:
- `A → B` ➡️
- `A → C` ➡️
- `A → D` ➡️

For each reachable node, I calculate the cost already traveled from the start: 📐
- `g(B) = g(A) + cost(A,B)`
- `g(C) = g(A) + cost(A,C)`
- `g(D) = g(A) + cost(A,D)`

---

## 📏 Heuristic Estimation

Then, for each reachable node, I look at the traversal information and calculate the Euclidean distance from that node to the goal. I will have a traversal/heuristic function for that. 📏🧠

So I update:
- `h(B) = estimated cost from B to the goal`
- `h(C) = estimated cost from C to the goal`
- `h(D) = estimated cost from D to the goal`

---

## 🧮 Calculating Total Cost f(n)

Then I calculate: 🧮
- `f(B) = g(B) + h(B)`
- `f(C) = g(C) + h(C)`
- `f(D) = g(D) + h(D)`

---

## 🔄 Iterative Loop & Path Optimization

- Then I choose the node with the smallest `f(n)`. ⭐
- That node becomes my current node, and I move to its reachable neighbors. 🏃‍♂️💨

For each new neighbor, I calculate the new cost from the start:
- `g(node) = g(current) + cost(current,node)`

Then I calculate the estimated cost to the goal:
- `h(node) = Euclidean distance(node, goal)`

And then:
- `f(node) = g(node) + h(node)`

I do the same process again and choose the node with the smallest `f(n)`. 🔄

I continue doing this until I reach the goal. 🏁

---

## 🔗 Tracking Paths & Re-visiting Nodes

At the same time, I need to keep track of the predecessor of each node so that, once I reach the goal, I can reconstruct the path that was found. 🧵🗺️

One important thing is that if I reach a node that I have already visited, I should compare the new `g(n)` with the previous `g(n)`. If the new path has a lower cost, I update the cost and the predecessor. 🔄💡
