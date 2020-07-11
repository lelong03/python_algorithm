# Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.
# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Ouptut: Sum found between indexes 2 and 4


def sub_arr_with_sum(arr, s):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j]) == s:
                return i, j-1
    return None


def sub_arr_with_sum_optimized(arr, s):
    start = 0
    current_sum = arr[start]
    for i in range(1, len(arr)):
        current_sum += arr[i]

        if current_sum > s:
            while current_sum > s and start < i:
                current_sum -= arr[start]
                start += 1

        if current_sum == s:
            return start, i

    return None


def sub_arr_with_sum_for_negative(arr, s):
    map = {}
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == s:
            return 0, i

        if current_sum - s in map:
            return map[current_sum - s] + 1, i
        else:
            map[current_sum] = i
            
    return None


arr = [1, 4, 20, 3, 10, 5]
s = 33

print(sub_arr_with_sum(arr, s))
print(sub_arr_with_sum_optimized(arr, s))


arr = [10, 2, -2, -20, 10]
s = -20
print(sub_arr_with_sum_for_negative(arr, s))
