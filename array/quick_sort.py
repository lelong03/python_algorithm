def quicksort(alist):
    quicksort_helper(alist, 0, len(alist)-1)


def quicksort_helper(alist, first, last):
    if last < first:
        return
    pivot = alist[first]
    split_point = partion(alist, first, last, pivot)

    quicksort_helper(alist, first, split_point-1)
    quicksort_helper(alist, split_point+1, last)


def partion(alist, first, last, pivot):
    pivot_idx = first
    first = first + 1
    while first <= last:
        while first <= last and alist[first] < pivot:
            first += 1

        while first <= last and alist[last] > pivot:
            last -= 1

        if first <= last:
            alist[first], alist[last] = alist[last], alist[first]

    alist[last], alist[pivot_idx] = alist[pivot_idx], alist[last]
    return last


# def partion(alist, first, last, pivot):
#     pivot_idx = first
#     first = pivot_idx + 1
#     while first <= last:
#         while first <= last and alist[first] < pivot:
#             first += 1
#
#         while first <= last and alist[last] > pivot:
#             last -= 1
#
#         if first <= last:
#             alist[first], alist[last] = alist[last], alist[first]
#
#     alist[last], alist[pivot_idx] = alist[pivot_idx], alist[last]
#     return last
#
#
# def find_kth_number(alist, k):
#     return find_kth_number_helper(alist, 0, len(alist)-1, k)
#
#
# def find_kth_number_helper(alist, first, last, k):
#     pivot = alist[first]
#     split_point = partion(alist, first, last, pivot)
#     if k == split_point:
#         return alist[k]
#     elif k < split_point:
#         return find_kth_number_helper(alist, first, split_point-1, k)
#     else:
#         return find_kth_number_helper(alist, split_point+1, last, k-split_point)


a = [10, 9, 5, 11, 15, 2, 4, 1, 18, 8]
quicksort(a)
print a
