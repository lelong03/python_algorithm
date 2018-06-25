# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.



def reverse(arr, begin, end):
    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1

def next_permutation(arr, begin, end):
    partion_index = end-1
    while partion_index > -1 and arr[partion_index] >= arr[partion_index+1]:
        partion_index -= 1
        
    if partion_index == -1:
        return reverse(arr, begin, end)
    
    change_index = end
    while change_index > -1 and arr[change_index] <= arr[partion_index]:
        change_index -= 1

    arr[change_index], arr[partion_index] = arr[partion_index], arr[change_index]
    return reverse(arr, partion_index+1, end)


a = [1,3,4,2]
next_permutation(a, 0, len(a)-1)
print a


a = [1,4,2,3]
next_permutation(a, 0, len(a)-1)
print a


a = [1,2,3,4]
next_permutation(a, 0, len(a)-1)
print a


a = [4,3,2,1]
next_permutation(a, 0, len(a)-1)
print a


a = [5,1,1]
next_permutation(a, 0, len(a)-1)
print a
