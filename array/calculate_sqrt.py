def mysqrt(n):
    start = 0
    end = n
    mid = float(end + start) / 2
    while ( (mid*mid) != n ) and ( abs((mid * mid) - n) > 0.1 ):
        if (mid*mid) > n:
            end = mid
        else:
            start = mid
        mid = float(end + start) / 2
    return mid

print(mysqrt(3))
