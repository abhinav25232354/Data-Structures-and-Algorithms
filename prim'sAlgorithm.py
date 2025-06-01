import heapq

def prim(graph, start=0):
    """
    graph: adjacency list with (neighbor, weight) pairs
    start: starting vertex
    """
    mst = []
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)
    
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for to_next, w in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (w, to, to_next))
    return mst


# Example graph as adjacency list: vertex -> list of (neighbor, weight)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

mst = prim(graph, start=0)
print("Prim's MST edges:")
for edge in mst:
    print(edge)
