import sys


class Graph(object):

    def __init__(self, graph):
        self.vertices = len(graph)
        self.graph = graph

    def get_min_vertex(self, dist, visited):
        min = sys.maxint
        for v in range(self.vertices):
            if not visited[v] and dist[v] < min:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, start_vertex):
        visited = [False] * self.vertices
        dist = [sys.maxint] * self.vertices
        dist[start_vertex] = 0
        for vertex in range(self.vertices):
            u = self.get_min_vertex(dist, visited)
            visited[u] = True
            for v in range(self.vertices):
                if not visited[v] and self.graph[u][v] > 0 and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        print(dist)


matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

g = Graph(matrix)
g.dijkstra(0)
