class sea_graph():
    def __init__(self, g):
        self.ROW = len(g)
        self.COL = len(g[0])
        self.graph = g

    def is_safe(self, r, c):
        return (r >= 0) and (r < self.ROW) and \
               (c >= 0) and (c < self.COL) and \
               (self.graph[r][c]) and (not self.visited[r][c])


    def DFS(self, r, c):
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.visited[r][c] = True
        for i in range(8):
            _r = r + row_nbr[i]
            _c = c + col_nbr[i]
            if self.is_safe(_r, _c):
                self.DFS(_r, _c)

    def count_island(self):
        self.visited = [[False for c in range(self.COL)] for r in range(self.ROW)]
        num_island = 0
        for r in range(self.ROW):
            for c in range(self.COL):
                if self.graph[r][c] and not self.visited[r][c]:
                    self.DFS(r, c)
                    num_island += 1
        return num_island

    def get_island_area(self, r, c, area):
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.visited[r][c] = True
        area += 1
        for i in range(8):
            _r = r + row_nbr[i]
            _c = c + col_nbr[i]
            if self.is_safe(_r, _c):
                return self.get_island_area(_r, _c, area)
        return area

    def get_bigest_area(self):
        self.visited = [[False for c in range(self.COL)] for r in range(self.ROW)]
        max = 0
        for r in range(self.ROW):
            for c in range(self.COL):
                if self.graph[r][c] and not self.visited[r][c]:
                    cell_count = self.get_island_area(r,c, 0)
                    if cell_count > max:
                        max = cell_count
        return max


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

my_graph = sea_graph(g=graph)
print my_graph.count_island()
print my_graph.get_bigest_area()

