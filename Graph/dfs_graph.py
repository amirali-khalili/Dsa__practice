def dfs_graph(graph,vertex=None,visited=None):
    if vertex is None:
        vertex = list(graph.keys())[0]
    if visited is None :
        visited = set()

    if vertex not in visited :
        print(vertex,end=" ")
        visited.add(vertex)
        for neighbor in graph[vertex] :
            dfs_graph(graph,neighbor,visited)




def dfs_iteative(graph):
    visited = set()
    start = list(graph.keys())[0]
    stack = []
    stack.append(start)

    while stack :
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}
print("Recursive graph: ")
dfs_graph(graph)

print("\nIterative graph: ")
dfs_iteative(graph)