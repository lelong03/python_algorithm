

def count_possible(digits, n, decoding):
    if n == 0 or n == 1:
        decoding[n] = 1
        return decoding[n]

    total = 0

    if digits[n-1] > '0':
        if decoding[n-1] == 0:
            decoding[n-1] = count_possible(digits, n-1, decoding)
        total = decoding[n-1]

    if (digits[n-2] == '1') or (digits[n-2] == '2' and digits[n-1] < '7'):
        if decoding[n-2] == 0:
            decoding[n-2] = count_possible(digits, n-2, decoding)
        total += decoding[n-2]

    decoding[n] = total
    # print decoding
    return total


def count_possible2(digits, n):
    decoding  = [0] * (n+1)
    decoding[0] = decoding[1] = 1
    for i in range(2, n+1):
        if digits[i-1] > '0':
            decoding[i] = decoding[i-1]

        if (digits[i - 2] == '1') or (digits[i - 2] == '2' and digits[i - 1] < '7'):
            decoding[i] = decoding[i] + decoding[i-2]
    # print decoding
    return decoding[n]

# digits = '1223574531212121542542511323212321212121121232'
digits = '1223'
n = len(digits)
decoding = [0] * (n+1)
print count_possible(digits, n, decoding)
print count_possible2(digits, n)