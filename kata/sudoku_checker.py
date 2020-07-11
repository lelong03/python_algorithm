def done_or_not(board):
    correct = [x + 1 for x in range(9)]

    for row in board:
        if sorted(row) != correct:
            return "Try again!"

    for col in zip(*board):
        if sorted(col) != correct:
            return "Try again!"

    for row in range(3):
        for col in range(3):
            squares = []
            for line in board[row*3:(row+1)*3]:
                squares = squares + line[col*3:(col+1)*3]
            if sorted(squares) != correct:
                return "Try again!"

    return "Finished!"



print done_or_not(
[[1, 3, 2, 5, 7, 9, 4, 6, 8]
,[4, 9, 8, 2, 6, 1, 3, 7, 5]
,[7, 5, 6, 3, 8, 4, 2, 1, 9]
,[6, 4, 3, 1, 5, 8, 7, 9, 2]
,[5, 2, 1, 7, 9, 3, 8, 4, 6]
,[9, 8, 7, 4, 2, 6, 5, 3, 1]
,[2, 1, 4, 9, 3, 5, 6, 8, 7]
,[3, 6, 5, 8, 1, 7, 9, 2, 4]
,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

print done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])