class KnightTour:
    def __init__(self, g):
        self.ROW = len(g)
        self.COL = len(g[0])
        self.GRAPH = g

    def is_safe(self, r, c):
        return (r >= 0) and (r < self.ROW) and \
                (r >= 0) and (c < self.COL) and \
                (self.GRAPH[r][c] == 0)

    def print_tour(self):
        for row in self.GRAPH:
            print row
        return True

    def make_tour(self):
        start_row, start_col = 0, 0
        self.GRAPH[start_row][start_col] = 1
        if self.try_tour(2, start_row, start_col):
            self.print_tour()
        else:
            print "No solution!"

    def try_tour(self, step_th, row, col):
        r_move = [2, 1, -1, -2, -2, -1, 1, 2]
        c_move = [1, 2, 2, 1, -1, -2, -2, -1]

        if step_th == self.ROW * self.COL:
            return True
        else:
            for j in range(8):
                next_row = row + r_move[j]
                next_col = col + c_move[j]
                if self.is_safe(next_row, next_col):
                    self.GRAPH[next_row][next_col] = step_th
                    if self.try_tour(step_th + 1, next_row, next_col):
                        return True
                    else:
                        self.GRAPH[next_row][next_col] = 0


graph = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]


graph = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
kt = KnightTour(graph)
kt.make_tour()

