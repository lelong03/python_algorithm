# Question: multiply two positive numbers without using * operator
# Solutions: with a * b, we try to count how many squares in the rectangle grid when the length and width of grid are a and b

def multiply(a, b):
    smaller = a if a < b else b
    bigger = (a+b) - smaller
    return multiply_helper(smaller, bigger)

def multiply_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    half_value = multiply_helper(smaller>>1, bigger)
    if smaller % 2 == 0:
        return half_value + half_value
    else:
        return half_value + half_value + bigger

print multiply(7, 8)

