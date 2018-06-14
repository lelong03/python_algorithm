import sys

class Graph():
    def __init__(self, g_nodes):
        self.vertex_num = g_nodes
        self.vertices = set(range(1, g_nodes+1))
        self.vertices_dict = {}

    def set_edge(self, p_from, p_to, p_weight):
        if p_from not in self.vertices_dict:
            self.vertices_dict[p_from] = {}
        self.vertices_dict[p_from].update({
            p_to: p_weight
        })

    def min_distance(self, Q, dist):
        min = sys.maxint
        min_index = None
        for i in range(len(dist)):
            if dist[i] < min and i in Q:
                min = dist[i]
                min_index = i
        return min_index

    def get_shortest_path(self, start, end):
        dist = [sys.maxint] * self.vertex_num
        dist[start] = 0
        S = set()
        Q = self.vertices.copy()
        while len(Q):
            u = self.min_distance(Q, dist)
            Q.remove(u)
            S.add(u)
            neighbors = self.vertices_dict[u]
            for nei in neighbors:
                weight = neighbors[nei]
                if dist[nei] > dist[u] + weight:
                    dist[nei] = dist[u] + weight
        return dist

    def __str__(self):
        return str(self.vertices_dict)


g = Graph(6)
g.set_edge(1, 2, 2)
g.set_edge(1, 3, 4)

g.set_edge(2, 3, 1)
g.set_edge(2, 4, 4)
g.set_edge(2, 5, 2)

g.set_edge(3, 5, 3)

g.set_edge(4, 6, 2)

g.set_edge(5, 4, 3)
g.set_edge(5, 6, 2)
print g

print g.get_shortest_path(1, 6)
