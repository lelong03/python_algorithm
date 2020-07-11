def longestChain(words):
    cache = {}
    words_set = set(words)
    gmax = 0
    for word in words:
        gmax = max(gmax, longest(words_set, cache, word))
    return gmax


def longest(words_set, cache, word):
    if word not in cache:
        ret = 1
        for i in range(len(word)):
            w = word[:i] + word[i+1:]
            if w and w in words_set:
                cnt = longest(words_set, cache, w)
                ret = max(ret, 1 + cnt)
        cache[word] = ret
    return cache[word]

words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(longestChain(words))


s = 'abcd'
for i in range(len(s)):
    print(s[:i] + s[i+1:])

