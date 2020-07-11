class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.count = 0

    def add_index(self, name, index):
        self.count += 1
        if index == len(name):
            return
        c = name[index]
        if c not in self.children:
            sub_node = TrieNode()
            self.children[c] = sub_node
        else:
            sub_node = self.children[c]
        sub_node.add_index(name, index+1)

    def find_index(self, name, index):
        if index == len(name):
            return self.count
        c = name[index]
        if c not in self.children:
            return 0
        sub_node = self.children[c]
        return sub_node.find_index(name, index+1)


root = TrieNode()


def add(name):
    root.add_index(name, 0)


def find(name):
    return root.find_index(name, 0)


add('lzrxegypcyyyjfszwrdu')
print(find('bomdf'))
