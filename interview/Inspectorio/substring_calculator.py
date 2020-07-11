class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


def all_substr(word):
    global root
    root = TrieNode()
    result = 0
    for s in range(0, len(word)):
        node = root
        sv = ord(word[s])
        if sv not in root.children:
            node.children[sv] = TrieNode()
        if not node.children[sv].end:
            result += 1
            node.children[sv].end = True
        node = node.children[sv]
        for e in range(1, len(word)):
            i = s + e
            if i >= len(word):
                break
            iv = ord(word[i])
            if iv not in node.children:
                node.children[iv] = TrieNode()
            if not node.children[iv].end:
                result += 1
                node.children[iv].end = True
            node = node.children[iv]

    return result


result = all_substr('kincenvizh')
print((result))


def count_substring(s):
    count = 0
    substring = set()

    for i in range(len(s)):
        sub = s[i:]
        sub_len = len(sub)
        for j in range(sub_len):
            sub_distinct = sub[0:sub_len-j]
            if sub_distinct in substring:
                continue
            substring.add(sub_distinct)
            # print(sub_distinct)
            count += 1
    return count

print(count_substring('kincenvizh'))
