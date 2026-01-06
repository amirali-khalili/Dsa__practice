class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []  
        self.vertex_data = [''] * size  

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u, v, weight))
            
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_edges(self):
        print("Edge \tWeight")
        for u, v, weight in self.edges:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")



g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(0, 1, 4) 
g.add_edge(0, 6, 10)  
g.add_edge(0, 2, 9)   
g.add_edge(1, 2, 8)   
g.add_edge(2, 3, 5) 
g.add_edge(2, 4, 2)  
g.add_edge(2, 6, 7)  
g.add_edge(3, 4, 3)  
g.add_edge(3, 5, 7) 
g.add_edge(4, 6, 6)  
g.add_edge(5, 6, 11)

print("Kruskal's Algorithm MST:")
g.print_edges()