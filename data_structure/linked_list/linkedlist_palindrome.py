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

def reverve_ll(ll):
    pre = None
    current = ll
    while current is not None:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre

def compare_ll(ll1, ll2):
    temp1 = ll1
    temp2 = ll2
    while temp1 is not None and temp2 is not None:
        if temp1.value != temp2.value:
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1 is None and temp2 is None:
        return True
    return False


def isListPalindrome(l):
    if l is None or l.next is None:
        return True
    slow_pointer = l
    fast_pointer = l
    prev_slow_pointer = l
    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        prev_slow_pointer = slow_pointer
        slow_pointer = slow_pointer.next

    prev_slow_pointer.next = None
    first_half = l
    if fast_pointer is not None:
        second_half = reverve_ll(slow_pointer.next)
    else:
        second_half = reverve_ll(slow_pointer)
    if compare_ll(first_half, second_half):
        return True
    return False

l = [10]
print isListPalindrome(l_to_ll(l))



