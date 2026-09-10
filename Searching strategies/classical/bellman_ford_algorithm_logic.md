# Bellman-Ford Algorithm Logic

Here is the refined and corrected logic for your Bellman-Ford core algorithm, organized for clarity and optimal pathfinding.

## 🚀 Algorithm Overview

* **Initialize distances:** Set the distance to the start node to `0` and all other nodes to `inf` (infinity).
* **Retrieve graph properties:** Get the total number of nodes ($V$) and all the edges of the graph.

---

## 📌 Step-by-Step Logic

1. **Relax edges $V - 1$ times:**
   * 🔄 Loop through a range of `number_of_nodes - 1` to ensure all shortest paths fully propagate and prevent infinite loops.
   * 🗺️ For each edge in the collection of edges:
     * 📥 **Retrieve variables:** Get the source node `u`, the target node `v`, and the edge weight `w`.
     * ⚖️ **Relaxation formula:** Calculate the potential new distance using `new_distance = min(dist[v], dist[u] + w)`.
     * ➕ **Update and track:** If the distance is minimized (`new_distance < dist[v]`), update `dist[v]` to the new distance and record `u` as the predecessor of `v` in your tracking dictionary.

2. **Check for negative weight cycles:**
   * ⚠️ Perform one final check across all edges after the main loops finish.
   * 🔍 Verify if further relaxation is still possible (`dist[u] + w < dist[v]`). If any distance can still be reduced, flag that a negative weight cycle exists.

---

💡 *Pro-tip: Remember to guard your relaxation step by checking `if self.distances[u] != float('inf'):` so you don't perform math on unreachable nodes!*
