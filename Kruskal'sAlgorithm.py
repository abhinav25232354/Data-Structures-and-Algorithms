class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # path compression
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return False
        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        elif self.rank[rootV] < self.rank[rootU]:
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1
        return True

def kruskal(edges, n):
    """
    edges: list of (weight, u, v)
    n: number of vertices
    """
    edges.sort()
    uf = UnionFind(n)
    mst = []
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
    return mst

# Example edges: (weight, u, v)
edges = [
    (2, 0, 1), (6, 0, 3), (3, 1, 2), (8, 1, 3), (5, 1, 4),
    (7, 2, 4), (9, 3, 4)
]

mst = kruskal(edges, 5)
print("\nKruskal's MST edges:")
for edge in mst:
    print(edge)
