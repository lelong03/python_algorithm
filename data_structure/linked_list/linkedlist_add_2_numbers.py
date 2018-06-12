# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def l_to_ll(l):
    if not l:
        return None

    root = cur_node = ListNode(l[0])
    for n in l[1:]:
        new_node = ListNode(n)
        cur_node.next = new_node
        cur_node = new_node

    return root

def ll_to_l(ll):
    l = []
    current_node = ll
    while current_node:
        l.append(current_node.value)
        current_node = current_node.next
    return l


def reverse_ll(ll):
    prev = None
    current = ll
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev



    while current:
        temp = current.next
        temp.next = current
        current.next = previous
        previous = current

def addTwoHugeNumbers(a, b):
    a1 = reverse_ll(a)
    b1 = reverse_ll(b)
    root = None
    current_node = root
    mem_value = 0
    while a1 or b1:
        a1_value = a1.value if a1 is not None else 0
        b1_value = b1.value if b1 is not None else 0
        total = a1_value + b1_value + mem_value
        mem_value = total // 10
        new_node = ListNode(total % 10)
        if root is None:
            root = new_node
            current_node = root
        else:
            current_node.next = new_node
            current_node = new_node
        a1 = a1.next if a1 is not None else None
        b1 = b1.next if b1 is not None else None
    if mem_value > 0:
        new_node = ListNode(mem_value)
        current_node.next = new_node
    return reverse_ll(root)



# a = [9876, 5432, 1999]
# b = [1, 8001]
# c = addTwoHugeNumbers(l_to_ll(a), l_to_ll(b))
# print ll_to_l(c)
#
# a = [123, 4, 5]
# b = [100, 100, 100]
# c = addTwoHugeNumbers(l_to_ll(a), l_to_ll(b))
# print ll_to_l(c)

a = [1]
b = [9999, 9999, 9999, 9999, 9999, 9999]
c = addTwoHugeNumbers(l_to_ll(a), l_to_ll(b))
print ll_to_l(c)


a = [2,3,5]
b = [2,3,5]
c = addTwoHugeNumbers(l_to_ll(a), l_to_ll(b))
print ll_to_l(c)