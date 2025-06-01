class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, bidirectional=True):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1].append(node2)
        if bidirectional:
            self.graph[node2].append(node1)

    def display(self):
        print("Graph adjacency list:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def simple_visualization(self):
        print("\nGraph visualization (node: neighbors):")
        for node, neighbors in self.graph.items():
            print(f"{node}: " + " —> ".join(str(n) for n in neighbors))

g = Graph()

# Add nodes and edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("E", "F")

g.display()

print("\nDFS Traversal from node A:")
g.dfs("A")

print("\n\nBFS Traversal from node A:")
g.bfs("A")

g.simple_visualization()

"""
Graph Theory and Types of Graphs:

A **Graph** is a collection of nodes (also called vertices) and edges that connect pairs of nodes.
Graphs are used extensively in computer science to model networks, relationships, and many real-world problems.

Types of Graphs:

1. Undirected Graph:
   - Edges have no direction.
   - If there is an edge between node A and node B, you can travel both ways: A ↔ B.
   - Represented as a set of vertices and unordered pairs of vertices.
   - Example: Social networks where friendships are mutual.

2. Directed Graph (Digraph):
   - Edges have a direction, going from one node to another.
   - Represented as ordered pairs (A → B).
   - Useful for modeling relationships like web page links, or task scheduling dependencies.
   - Example: Twitter follower relationships (A follows B but not necessarily vice versa).

3. Weighted Graph:
   - Edges carry weights (values) representing cost, distance, or capacity.
   - Can be directed or undirected.
   - Used in shortest path problems, network routing, etc.
   - Example: Road maps where edges represent distances between cities.

4. Unweighted Graph:
   - Edges do not have weights.
   - The presence or absence of an edge is the only concern.

5. Simple Graph:
   - No loops (edges connecting a node to itself).
   - No multiple edges between the same two nodes.

6. Multigraph:
   - Can have multiple edges between the same two nodes.
   - Useful for modeling parallel connections or multiple relationships.

7. Cyclic and Acyclic Graphs:
   - Cyclic: Contains at least one cycle (a path starting and ending at the same node).
   - Acyclic: Contains no cycles.
   - Example: Trees are acyclic graphs.

8. Connected and Disconnected Graphs:
   - Connected: There is a path between every pair of nodes.
   - Disconnected: Some nodes cannot be reached from others.

9. Tree:
   - A special type of connected, acyclic, undirected graph.
   - Often used to represent hierarchical data.

Graph Representations:

1. Adjacency Matrix:
   - A 2D matrix where cell (i, j) indicates presence/weight of edge between node i and j.
   - Efficient for dense graphs but uses more space.

2. Adjacency List:
   - Each node stores a list of adjacent nodes.
   - More space-efficient for sparse graphs.
   - Easier to traverse neighbors.

Common Graph Algorithms:

1. Traversal:
   - Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
   - Breadth-First Search (BFS): Explores neighbors level by level.

2. Shortest Path:
   - Dijkstra’s Algorithm: For weighted graphs with non-negative weights.
   - Bellman-Ford Algorithm: Handles negative weights.

3. Minimum Spanning Tree:
   - Kruskal’s and Prim’s algorithms find a subset of edges connecting all nodes with minimum total weight.

4. Topological Sorting:
   - Orders nodes linearly for Directed Acyclic Graphs (DAGs).
   - Useful in scheduling tasks.

5. Cycle Detection:
   - Important to identify cycles in directed or undirected graphs.

Applications of Graphs:

- Social Networks (friendships, followers)
- Computer Networks (routers, links)
- Web Page Link Structure
- GPS and Navigation Systems
- Scheduling and Task Planning
- Recommendation Systems
- Biological Networks (protein interactions)
- Many more!

Why Learn Graphs?

Graphs are fundamental to many computer science problems and real-world applications.
Understanding graphs, their types, and algorithms equips you to solve complex problems involving relationships and networks effectively.

"""