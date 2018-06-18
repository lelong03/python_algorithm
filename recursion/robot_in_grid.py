# ROBOT IN GRID
# Design an algorithm to find a path for the robot from the top left to the bottom right


def find_path(matrix, row, col, path, failed_list):
    if row < 0 or col < 0:
        return False
    if [row, col] in failed_list:
        return False
    at_origin = row == 0 and col == 0
    if at_origin \
            or find_path(matrix, row - 1, col, path, failed_list) \
            or find_path(matrix, row, col - 1, path, failed_list):
        path.append([row, col])
        return True
    failed_list.append([row, col])
    return False


def main(matrix):
    if matrix is None or len(matrix) <= 0:
        return None
    failed_list = []
    path = []
    if find_path(matrix, len(matrix) - 1, len(matrix[0]) - 1, path, failed_list):
        return path
    return None


maze = [[False for c in range(6)] for r in range(3)]
print(main(maze))

