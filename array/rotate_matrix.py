class Matrix(object):
    """
    Matrix class - Rotate matrix
    """

    def __init__(self, a_matrix):
        self.ROW = len(a_matrix)
        self.COL = len(a_matrix[0])
        self.A = a_matrix

    def show(self):
        """
        use to print matrix on screen
        """
        for r in self.A:
            print(r)

    def rotate_left_with_space(self):
        """
        rotate matrix to left side. this function is using extra memory to store extra 2D array
        can use it to rotate any matrix
        """
        ex_matrix = [[0 for r in range(self.ROW)] for c in range(self.COL)]
        for r in range(self.ROW):
            for c in range(self.COL):
                ex_matrix[self.COL - 1 - c][r] = self.A[r][c]
        self.A = ex_matrix

    def rotate_left_inplace(self):
        """
        rotate matrix to left side without using extra memory
        however, only use it when number of rows equals with number of columns
        """
        n = self.ROW
        for x in range(0, int(n / 2)):
            for y in range(x, n - 1 - x):
                temp = self.A[x][y]
                self.A[x][y] = self.A[y][n - 1 - x]
                self.A[y][n - 1 - x] = self.A[n - 1 - x][n - 1 - y]
                self.A[n - 1 - x][n - 1 - y] = self.A[n - 1 - y][x]
                self.A[n - 1 - y][x] = temp

    def rotate_left(self):
        if self.ROW != self.COL:
            self.rotate_left_with_space()
        else:
            self.rotate_left_inplace()

    def rotate_right_inplace(self):
        """
        rotate matrix to right side without using extra memory
        however, only use it when number of rows equals with number of columns
        """
        n = self.ROW
        for x in range(int(n/2)):
            for y in range(x, n-1-x):
                temp = self.A[x][y]
                self.A[x][y] = self.A[n-1-y][x]
                self.A[n-1-y][x] = self.A[n-1-x][n-1-y]
                self.A[n-1-x][n-1-y] = self.A[y][n-1-x]
                self.A[y][n-1-x] = temp

    def rotate_right_with_space(self):
        """
        rotate matrix to right side. this function is using extra memory to store extra 2D array
        can use it to rotate any matrix
        """
        ex_matrix = [[0 for r in range(self.ROW)] for c in range(self.COL)]
        for r in range(self.ROW):
            for c in range(self.COL):
                ex_matrix[c][self.ROW - 1 - r] = self.A[r][c]
        self.A = ex_matrix

    def rotate_right(self):
        if self.ROW != self.COL:
            self.rotate_right_with_space()
        else:
            self.rotate_right_inplace()


if __name__ == '__main__':
    print("-----------ROTATE LEFT------------")
    mat1 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    my_matrix = Matrix(mat1)
    my_matrix.rotate_left()
    my_matrix.show()

    print("-----------ROTATE LEFT------------")

    mat2 = [[1, 2],
            [5, 6],
            [9, 10],
            [13, 14]]
    my_matrix = Matrix(mat2)
    my_matrix.rotate_left()
    my_matrix.show()

    print("-----------ROTATE RIGHT-----------")

    mat3 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    my_matrix = Matrix(mat3)
    my_matrix.rotate_right()
    my_matrix.show()

    print("-----------ROTATE RIGHT-----------")

    mat4 = [[1, 2],
            [5, 6],
            [9, 10],
            [13, 14]]
    my_matrix = Matrix(mat4)
    my_matrix.rotate_right()
    my_matrix.show()

