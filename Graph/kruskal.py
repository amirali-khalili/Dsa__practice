def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            edges.append((w, u, v))
    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    mst = []
    total_weight = 0

    for w, u, v in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, w))
            total_weight += w
           


    return mst, total_weight
graph = {
    'A': {'B': 2, 'C': 70, 'D': 10},
    'B': {'A': 2, 'C': 8, 'D': 2},
    'C': {'A': 70, 'B': 8, 'D': 1},
    'D': {'A': 10, 'B': 2, 'C': 1},
}


mst, cost = kruskal(graph)
print("yal ha MST:", mst)
print("vazn kol:", cost)
