def minimumBribes(q):
    swap_count = 0
    len_q = len(q)
    for i in range(len_q):
        j = i+1
        temp_count = 0
        while j < len_q:
            if q[j] < q[i]:
                temp_count += 1
            if temp_count > 2:
                return "Too chaotic"
            j += 1
        swap_count += temp_count
    return swap_count


print(minimumBribes([2, 1, 5, 3, 4]))
print(minimumBribes([2, 5, 1, 3, 4]))
print(minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]))

