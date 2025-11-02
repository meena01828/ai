import sys

def dijkstra(graph, src):
    V = len(graph)
    dist = [sys.maxsize] * V
    dist[src] = 0
    sptSet = [False] * V

    for _ in range(V):
        min_dist = sys.maxsize
        u = -1
        for v in range(V):
            if not sptSet[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        sptSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not sptSet[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print("Vertex \tDistance from Source")
    for i in range(V):
        print(f"{i} \t{dist[i]}")

graph = [
    [0, 10, 0, 5],
    [0, 0, 1, 2],
    [0, 0, 0, 0],
    [0, 3, 9, 0]
]
dijkstra(graph, 0)
