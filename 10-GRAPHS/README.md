## Graphs in Data Structures (Python)

### 1. What is a Graph?

A **graph** is a non-linear data structure consisting of **vertices (nodes)** and **edges** that connect pairs of vertices.

Real-world examples:

* Social networks (people & connections)
* Road maps
* Computer networks
* Recommendation systems

---

### 2. Basic Terminology

* **Vertex (Node)**: An entity in the graph
* **Edge**: Connection between two vertices
* **Degree**: Number of edges connected to a vertex
* **Path**: Sequence of vertices
* **Cycle**: Path that starts and ends at the same vertex

---

### 3. Types of Graphs

* Undirected Graph
* Directed Graph (Digraph)
* Weighted Graph
* Unweighted Graph
* Cyclic & Acyclic Graph

---

### 4. Graph Representation

#### 4.1 Adjacency List (Most Used)

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

#### 4.2 Adjacency Matrix

```python
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
```

---

### 5. Breadth First Search (BFS)

Uses a **queue** and explores level by level.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
```

---

### 6. Depth First Search (DFS)

Uses **recursion or stack**.

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

### 7. Time Complexity

| Traversal | Complexity |
| --------- | ---------- |
| BFS       | O(V + E)   |
| DFS       | O(V + E)   |

---

### 8. Applications of Graphs

* GPS navigation
* Social media analysis
* Network routing
* Dependency resolution
* AI path finding

---

### 9. Common Interview Questions

* Detect cycle in a graph
* Connected components
* Shortest path problems
* Topological sorting
* BFS vs DFS differences

---

### 10. Summary

Graphs are one of the most powerful and frequently used data structures. Mastering BFS and DFS is essential for interviews and real-world problem solving.
**AUTHORS:** NITHIN KUMAR Y
