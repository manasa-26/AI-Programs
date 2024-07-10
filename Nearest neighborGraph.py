from typing import List

def nearest_neighbor(graph: List[List[int]], start: int) -> int:
    V = len(graph)
    visited = [False] * V
    path = []
    visited[start] = True
    path.append(start)

    for _ in range(V - 1):
        min_distance = float('inf')
        next_vertex = 0
        for i in range(V):
            if not visited[i] and graph[path[-1]][i] < min_distance:
                min_distance = graph[path[-1]][i]
                next_vertex = i
        visited[next_vertex] = True
        path.append(next_vertex)
    cost = 0
    for i in range(V - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][start]
    return cost,path

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
start = 0
print(nearest_neighbor(graph, start))
