# Find median of two sorted arrays of same size
# Objective:  Given two sorted arrays of size n.
# Write an algorithm to find the median of combined array (merger of both the given arrays, size = 2n).


# What is Median?
# If n is odd then Median (M) = value of ((n + 1)/2)th item term.
# If n is even then Median (M) = value of [(n/2)th item term + (n/2 + 1)th item term]/2


# Binary Approach: Compare the medians of both arrays?
# - Say arrays are array1[] and array2[].
# - Calculate the median of both the arrays, say m1 and m2 for array1[] and array2[].
# - If m1 == m2 then return m1 or m2 as final result.
# - If m1 > m2 then median will be present in either of the sub arrays.

# - If m2 > m1 then median will be present in either of the sub arrays.

# - Repeat the steps from 1 to 5 recursively until 2 elements are left in both the arrays.
# - Then apply the formula to get the median
# - Median = (max(array1[0],array2[0]) + min(array1[1],array2[1]))/2

def get_median_and_index(l, start, end):
    size = end - start + 1
    if size % 2 != 0:
        index = start+(size+1)/2-1
        return index, l[index]
    else:
        index = start+size/2
        return (l[index] + l[index+1])

def find(a, a_start, a_end, b, b_start, b_end):
    if (a_end - a_start + 1) == 2 and (b_end - b_start + 1) == 2:
        return (max(a[a_start], b[b_start]) + min(a[a_end], b[b_end])) / 2

    mid_index_a, median_a = get_median_and_index(a, a_start, a_end)
    mid_index_b, median_b = get_median_and_index(b, b_start, b_end)

    if median_a == median_b:
        return median_a

    if median_a > median_b:
        return find(a, a_start, mid_index_a, b, mid_index_b, b_end)
    else:
        return find(a, mid_index_a, a_end, b, b_start, mid_index_b)

def get_median_of_two_sorted_arrays(array_1, array_2):
    return find(array_1, 0, len(array_1)-1, array_2, 0, len(array_2)-1)


if __name__ == '__main__':
    arr_1 = [2,6,9,10,11]
    arr_2 = [1,5,7,12,15]
    print(get_median_of_two_sorted_arrays(arr_1, arr_2))
