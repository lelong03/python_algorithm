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


def mergeTwoLinkedLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.value < l2.value:
        root = l1
        l1 = l1.next
    else:
        root = l2
        l2 = l2.next
    current = root
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l2 is not None:
        current.next = l2
    if l1 is not None:
        current.next = l1
    return root


l1 = [1, 2, 3, 9]
l2 = [4, 5, 6, 7, 8]

l1 = []
l2 = [1, 1, 2, 2, 4, 7, 7, 8]

l3 = mergeTwoLinkedLists(l_to_ll(l1), l_to_ll(l2))
print ll_to_l(l3)