def delete_duplicated_items(alist):
    if len(alist) == 0:
        return 0
    write_index = 0
    for i in range(1, len(alist)):
        if alist[write_index] != alist[i]:
            alist[write_index + 1] = alist[i]
            write_index += 1
    return write_index


a = [1,2,2,3,4,5,5,8,9,10,11,11,11,13,13,15]
unique_items = delete_duplicated_items(a)
print(unique_items)
print(a)
