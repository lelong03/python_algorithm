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

def removeKFromList(l, k):
    previous_node = None
    root = current_node = l
    while current_node is not None:
        if current_node.value == k:
            if previous_node is None:
                root = current_node.next
            else:
                previous_node.next = current_node.next
        else:
            previous_node = current_node
        current_node = current_node.next
    return root

sample_list = [3, 1, 2, 3, 4, 5]
k = 3
res = removeKFromList(l_to_ll(sample_list), k)
print ll_to_l(res)



