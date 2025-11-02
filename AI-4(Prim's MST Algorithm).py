import sys

def prim_mst(graph):
    V = len(graph)
    selected = [False] * V
    selected[0] = True
    edges = []

    for _ in range(V - 1):
        min_edge = sys.maxsize
        u, v = -1, -1
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and 0 < graph[i][j] < min_edge:
                        min_edge = graph[i][j]
                        u, v = i, j
        edges.append((u, v, min_edge))
        selected[v] = True

    print("Edges in MST using Prim's Algorithm:")
    total = 0
    for u, v, w in edges:
        print(f"{u} -- {v} == {w}")
        total += w
    print("Total Cost:", total)

# Example graph as adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)
