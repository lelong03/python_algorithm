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


def reverseNodesInKGroups(l, k):
    temp_list = []
    result = []
    while l is not None:
        temp_list.append(l.value)
        if len(temp_list) == k :
            temp_list = temp_list[::-1]
            result = result + temp_list
            temp_list = []
        l = l.next
    if len(temp_list):
        result = result + temp_list
    if not result:
        return None
    root = cur_node = ListNode(result[0])
    for i in result[1:]:
        new_node = ListNode(i)
        cur_node.next = new_node
        cur_node = new_node
    return root



l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 3


l1 = reverseNodesInKGroups(l_to_ll(l), k)
print ll_to_l(l1)