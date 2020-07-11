def lcs1(str1, str2, l1, l2):
    if l1 == 0 or l2 == 0:
        return 0
    if str1[l1-1] == str2[l2-1]:
        return 1 + lcs1(str1, str2, l1-1, l2-1)
    else:
        return max(lcs1(str1, str2, l1-1, l2), lcs1(str1, str2, l1, l2-1))


str1 = "AGGTAB"
str2 = "GXTXAYB"
l1 = len(str1)
l2 = len(str2)

# print lcs1(str1, str2, l1, l2)


def lcs(X, Y):
    row = len(X)
    column = len(Y)
    L = [[None] * (column+1) for i in xrange(row+1)]
    for i in range(row+1):
        for j in range(column+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print L

    i = row
    j = column
    res = []
    while i > 0 and j > 0:
        if L[i][j] == L[i-1][j-1] + 1:
            res.append(X[i-1])
            i = i -1
            j = j -1
        elif L[i][j] == L[i-1][j]:
            i = i-1
        else:
            j = j-1
    print "".join(res[::-1])
    return L[row][column]

X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)