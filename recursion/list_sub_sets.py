# Question: List all sub sets of one set
# Solutions:
# - with base case n = 0, there is one sub set {}
# - with n = 1, there are: {}, {a}
# - with n = 2, there are: {}, {a}, {b}, {a,b}
# - with n = 3, there are: {}, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}
# P(3) = P(2) + {c}


# Using Recursion
def list_sub_set(a_set, n):
    set_len = n + 1
    if set_len == 0:
        return [[]]
    result = []
    for subset in list_sub_set(a_set, n-1):
        result.append(subset)
        result.append(subset + list(a_set[n]))
    return result


# Combinatorics
def list_sub_set_2(a_set):
    set_length = len(a_set)
    max = 1 << set_length
    result = []
    for i in range(max):
        result.append(get_sub_set(a_set, set_length, i))
    return result

def get_sub_set(a_set, set_length, number):
    sub_set = []
    index = set_length-1
    while number > 0:
        if (number & 1) == 1:
            sub_set.append(a_set[index])
        index -= 1
        number >>= 1
    return sub_set


aset = ['a', 'b', 'c']
print list_sub_set(aset, len(aset)-1)

aset = ['a', 'b', 'c', 'd']
print list_sub_set_2(aset)