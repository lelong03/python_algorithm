def count_consecutive_sum(number):
    if number <= 0:
        return 0
    L, count = 1, 0
    while (L * (L+1)) < (2 * number):
        a = (1.0 * number - (L*(L+1)) / 2) / (L + 1)
        if a - int(a) == 0.0:
            count += 1
        L += 1
    return count


print (count_consecutive_sum(6))
