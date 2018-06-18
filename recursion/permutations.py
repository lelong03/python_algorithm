# Compute all permutations of a string

def gen_permutations(str, n):
    if n == 0:
        return []
    ch = str[n-1]
    for temp in gen_permutations(str, n-1):
        pass
