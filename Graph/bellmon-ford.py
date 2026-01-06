def bellman_ford_dict(graph, start):
    INF = float('inf')
    
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v, graph[u][v]))
    print(edges)
    dist = {node: INF for node in graph}
    dist[start] = 0

    for _ in range(len(graph)-1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            print("❌ manfiiiiii!")
            return None

    return dist
 

graph = {
    'A': {'B': 2, 'C': -5},
    'B': {'C': -1, 'D': 1},
    'C': {'D': 1,'A':6},
    'D': {'C':1}
}

result = bellman_ford_dict(graph, 'A')
print("Falsele A:", result)
