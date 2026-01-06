
def prim(graph, start):
    mst = []
    visited = set([start])
    edges = []

    for v, w in graph[start].items():
        edges.append((w, start, v))

    total_cost = 0

    while edges:
        edges.sort(key=lambda x: x[0])
        w, u, v = edges.pop(0)   

        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            total_cost += w
            for to, weight in graph[v].items():

                if to not in visited:
                    edges.append((weight, v, to))

    print("MST END:", mst)
    print("KOLI MST:", total_cost)







graph = {
    'A': {'B': 2, 'C': 70, 'D': 10},
    'B': {'A': 2, 'C': 8, 'D': 2},
    'C': {'A': 70, 'B': 8, 'D': 1},
    'D': {'A': 10, 'B': 2, 'C': 1},
}

prim(graph, 'A')
