# Uniform Cost Search (UCS) Algorithm Logic

Here is the refined and corrected logic for your Uniform Cost Search core algorithm, optimized for clarity and correct implementation.

## 🚀 Algorithm Overview

* **Initiate a counter** to handle tie-breaking for nodes with the same cumulative cost (preventing comparison errors in the priority queue).
* **Create a min-heap priority queue (`pq`)** represented as a list, containing:
  1. The initial cost (`0`).
  2. The counter value.
  3. The start node.
  4. The initial path containing the start node.

---

## 📌 Step-by-Step Logic

1. **While the heap is not empty:**
   * 📥 **Pop** the minimum element from the heap and unpack its variables (`cost`, `counter`, `current`, `path`).
   * 🔍 **Check visited status:** If the current node has already been visited, `continue` to the next iteration. Otherwise, mark it as visited.
   * 🎯 **Goal check:** If `current == goal`, return the path.
   * 🗺️ **Expand neighbors:** Get the neighbors of the current node using `self.graph.get_neighbors(current)`.

2. **For each neighbor `n`:**
   * ⚖️ **Calculate edge cost:** Use `self.graph.get_edges_weights(current, n)` *(Note: Ensure you pass `current` and `n` here to get the correct weight from the current node to its neighbor, rather than `start`)*.
   * ➕ **Calculate total cost:** `total_cost = cumulative_cost + cost`.
   * 📦 **Push to heap:** Push a tuple `(total_cost, next(counter), n, path + [n])` into the heap.

3. **Fallback:**
   * ❌ **Return `None`** if the heap becomes empty without reaching the goal.

---

💡 *Pro-tip: Keep your graph methods clean and ensure your tie-breaker counter uses `itertools.count()` for seamless Python implementation!*
