class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)] 
        self.size = [1]*n                     

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:   
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
dsu = DSU(5)
dsu.union(0,1)
dsu.union(3,4)
dsu.union(1,4)

print(dsu.find(0) == dsu.find(4))  # True
print(dsu.find(2) == dsu.find(3))  # False
