import heapq 

graph = {
    'A': {'B': 2, 'C': 6},
    'B': {'C': 3, 'D': 1},
    'C': {'D': 1},
    'D': {'C':1, 'A':4}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0  

    pq = [(0, start)] 
    
    while pq: 
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  
            if distance < distances[neighbor]:
                distances[neighbor] = distance 
                heapq.heappush(pq, (distance, neighbor))  

    return distances    

print(dijkstra(graph, 'A'))
