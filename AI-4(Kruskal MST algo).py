class GraphK:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph.sort(key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Edges in MST using Kruskal's Algorithm:")
        total = 0
        for u, v, w in result:
            print(f"{u} -- {v} == {w}")
            total += w
        print("Total Cost:", total)

gk = GraphK(4)
gk.add_edge(0, 1, 10)
gk.add_edge(0, 2, 6)
gk.add_edge(0, 3, 5)
gk.add_edge(1, 3, 15)
gk.add_edge(2, 3, 4)
gk.kruskal_mst()
