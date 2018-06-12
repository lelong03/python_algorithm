def max_sum(a):
    len_a = len(a)
    max = 0
    for i in range(len_a):
        sum_a = 0
        for j in range(i, len_a):
            sum_a += a[j]
            if sum_a > max:
                max = sum_a
    return max


alist = [-3, -4, 6, -2, -3, 2, -1, 6, 10]
print alist
print max_sum(alist)
