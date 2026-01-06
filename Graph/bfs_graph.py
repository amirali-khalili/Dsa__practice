from collections import deque

def bfs_graph(graph):
    start= list(graph.keys())[0]
    visited = set()
    queue = deque([start])

    while queue :
            node = queue.popleft()
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)    

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A'},
    'D': {'B'},
    'E': {'B'}
}

bfs_graph(graph)



