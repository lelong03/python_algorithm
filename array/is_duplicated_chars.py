

def is_unique_chars(my_str):
    checker = 0
    for c in my_str:
        bit_index = ord(c) - ord('a')
        if checker & (1 << bit_index) != 0:
            return False
        checker = checker | (1 << bit_index)
    return True


print(is_unique_chars('dbcad'))
