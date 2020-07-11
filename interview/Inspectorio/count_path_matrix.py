def numberOfPaths(a):
    if a[0][0] == 0:
        return 0
    row = len(a)
    col = len(a[0])

    result = []
    for item in a:
        result.append(item)

    min_k = min(row, col)
    for k in range(1, min_k):
        if a[k][k] == 0:
            continue
        result[k][k] = result[k][k - 1] + result[k-1][k]

        for j in range(k+1, col):
            if a[k][j] == 0:
                continue
            result[k][j] = result[k][j-1] + result[k-1][j]

        for i in range(k+1, row):
            if a[i][k] == 0:
                continue
            result[i][k] = result[i][k-1] + result[i-1][k]

    print(result)
    return result[row-1][col-1]



a = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(numberOfPaths(a))


b = [[1,1,1],[1,1,1],[1,0,1]]
print(numberOfPaths(b))

c = [[1]]
print(numberOfPaths(c))