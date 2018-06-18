# def bin_search(arr, item):
#     low = 0
#     high = len(arr) - 1
#     if item < arr[low]:
#         return 0
#     if item > arr[high]:
#         return high + 1
#     while low <= high:
#         middle = (low + high) / 2
#         if item == arr[middle]:
#             return middle+1
#         if item > arr[middle]:
#             low = middle+1
#         else:
#             high = middle-1
#     return high
#
# def count_elements(arr1, arr2):
#     arr1.sort()
#     print arr1
#     result = []
#     for item in arr2:
#         result.append(bin_search(arr1, item))
#     return result
#
#
# first = [4,7,1,6,2,3,5,9]
# second = [8]
# print count_elements(first, second)


# python implementation of For each element in 1st
# array count elements less than or equal to it
# in 2nd array

# function returns the index of largest element
# smaller than equal to 'x' in 'arr'. For duplicates
# it returns the last index of occurrence of required
# element. If no such element exits then it returns -1
def bin_search(arr, n, x):
    l = 0
    h = n - 1
    while (l <= h):
        mid = int((l + h) / 2)
        # if 'x' is greater than or equal to arr[mid],
        # then search in arr[mid + 1...h]
        if (arr[mid] <= x):
            l = mid + 1;
        else:
        # else search in arr[l...mid-1]
            h = mid - 1
    # required index
    return h


# function to count for each element in 1st array,
# elements less than or equal to it in 2nd array
def countElements(arr1, arr2, m, n):


    # sort the 2nd array
    arr2.sort()

    # for each element in first array
    for i in range(m):
        # last index of largest element
        # smaller than or equal to x
        index = bin_search(arr2, n, arr1[i])
        # required count for the element arr1[i]
        print(index + 1)

# driver program to test above function
arr1 = [1, 2, 3, 4, 7, 9]
arr2 = [0, 1, 2, 1, 1, 4]
first = [4,7,1,6,2,3,5,9]
second = [8]
m = len(arr1)
n = len(arr2)
print countElements(second, first, m, n)
