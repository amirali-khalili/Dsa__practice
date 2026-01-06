import heapq

def a_star(graph, start, goal, h):
    g = {node: float('inf') for node in graph}
    g[start] = 0

    f = {node: float('inf') for node in graph}
    f[start] = h[start]

    came_from = {}

    open_set = [(f[start], start)]

    while open_set:
        _ , current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g[goal]

        for neighbor, cost in graph[current].items():
            tentative_g = g[current] + cost
            if tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = g[neighbor] + h[neighbor]
                heapq.heappush(open_set, (f[neighbor], neighbor))

    return None, float('inf')


graph = {
    'A': {'B': 2, 'C': 6},
    'B': {'C': 3, 'D': 1},
    'C': {'D': 1},
    'D': {'C': 1, 'A': 4}
}

h = {
    'A': 4,
    'B': 1,
    'C': 1,
    'D': 0
}

path, cost = a_star(graph, 'A', 'D', h)
print("Road:", path)
print("Cost:", cost)
