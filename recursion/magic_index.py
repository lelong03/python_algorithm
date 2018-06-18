# A magic index in an array is defined to be an index such that A[i] = i
# Question: Finding the magic index in sorted array. Return -1 if not existed
# Solution:
# - Because of A is sorted array, should use binary search
# - Compare index with value (Note: index is increasing by 1, but value is increasing by more than 1


def find_magic_index(array_list, left, right):
    if left > right:
        return -1
    middle = int((left + right) / 2)
    if array_list[middle] == middle:
        return middle
    elif array_list[middle] > middle:
        return find_magic_index(array_list, left, middle - 1)
    else:
        return find_magic_index(array_list, middle + 1, right)


a = [-20, -40, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(find_magic_index(a, 0, len(a)-1))


# Question: if the elements of array are not not distinct, how to solve this problem
# Solution: check 2 both left and right but we try to minimize the range by different value from index i and A[i]

def find_magic_index_extend(array_list, left, right):
    if left > right:
        return -1

    middle = int((left + right) / 2)
    if array_list[middle] == middle:
        return middle

    # search left
    left_min_index = min(middle - 1, array_list[middle])
    index = find_magic_index_extend(array_list, left, left_min_index)
    if index > 0:
        return index

    # search right
    right_max_index = max(middle+1, array_list[middle])
    index = find_magic_index_extend(array_list, right_max_index, right)
    return index
