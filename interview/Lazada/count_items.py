def solution(A):
    if A[0] == -1:
        return 1
    flags = [False] * len(A)
    item_count = 1
    next_index = A[0]
    flags[0] = True

    while (A[next_index] != -1 and flags[next_index] is False):
        item_count += 1
        flags[next_index] = True
        next_index = A[next_index]

    if A[next_index] == -1:
        return item_count + 1
    return item_count


A = [1,4,-1,3,2]
print(solution(A))

B = [2,0,1]
print(solution(B))