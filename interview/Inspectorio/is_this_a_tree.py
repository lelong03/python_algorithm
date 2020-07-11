class Node(object):
    def __init__(self):
        self.value = None
        self.children = []

    def __str__(self):
        return '{%s:%s}' % (self.value, self.children)


root = None
node_list = {}
passed_nodes = set()
prev_val = None


def is_binary_tree(list_tuples):
    s = construct_tree(list_tuples)
    if s != 'S':
        return s
    s = is_cycle()
    if s != 'S':
        return s
    global root
    if not is_bst(root):
        return 'E5'
    return print_result(root)


def print_result(node):
    if node is None:
        return ""
    result = node.value
    if len(node.children) == 1:
        result = node.value + print_result(node.children[0])
    if len(node.children) == 2:
        if node.children[0].value > node.children[1].value:
            result += print_result(node.children[1]) + print_result(node.children[0])
        else:
            result += print_result(node.children[0]) + print_result(node.children[1])
    return '(' + result + ')'


def construct_tree(input_list):
    global node_list
    global root
    not_root = set()
    for edge in input_list:
        if edge[0] not in node_list:
            node_list[edge[0]] = Node()
            node_list[edge[0]].value = edge[0]
        if edge[1] not in node_list:
            node_list[edge[1]] = Node()
            node_list[edge[1]].value = edge[1]
        if len(node_list[edge[0]].children) >= 2:
            return 'E1'
        if len(node_list[edge[0]].children) > 0 and node_list[edge[0]].children[0].value == edge[1]:
            return 'E2'
        not_root.add(edge[1])
        node_list[edge[0]].children.append(node_list[edge[1]])
    if len(node_list) - len(not_root) > 1:
        return 'E4'
    for key, node in node_list.iteritems():
        if node not in not_root:
            root = node
            break
    return 'S'


def is_cycle():
    global node_list
    global root
    s = is_cycle_traverse(root)
    if not s:
        return 'E3'
    if len(node_list) - len(passed_nodes) > 0:
        return 'E4'
    return 'S'


def is_cycle_traverse(node):
    global passed_nodes
    if node is None:
        return True
    if node.value in passed_nodes:
        return False
    passed_nodes.add(node.value)
    if node.children:
        is_cycle_traverse(node.children[0])
        if len(node.children) > 1:
            is_cycle_traverse(node.children[1])
    return True


def is_bst(node):
    if node is None:
        return True
    if len(node.children) == 2:
        if node.children[0].value > node.children[1].value:
            node.children[0], node.children[1] = node.children[1], node.children[0]
    if len(node.children) > 0 and not is_bst(node.children[0]):
        return False
    global prev_val
    if prev_val is None:
        prev_val = node.value
    if len(node.children) <= 2:
        return True
    return is_bst(node.children[1])


if __name__ == '__main__':
    print(is_binary_tree([('B', 'D'), ('D', 'E'), ('A', 'B'), ('C', 'F'), ('E', 'G'), ('A', 'C')]))
    # print(is_binary_tree([('B', 'D'), ('D', 'E'), ('A', 'B'), ('C', 'F'), ('E', 'G'), ('B', 'C')]))




