def parity(x):
    result = 0
    while x:
        result ^= x & 1
        # print(result)
        x >>= 1
        # print(x)
    return result

n = 8
print(bin(n))
print(parity(n))
