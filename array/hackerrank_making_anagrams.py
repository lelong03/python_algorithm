# Given two strings ,a  and b, that may or may not be of the same length,
# determine the minimum number of character deletions required to make a and b anagrams.
# Any characters can be deleted from either of the strings.

# link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem




def str_to_dict(str):
    if str is None:
        return None
    if len(str) == 0:
        return {}
    str_dict = {}
    for c in str:
        if c not in str_dict:
            str_dict[c] = 1
        else:
            str_dict[c] += 1
    return str_dict


def make_anagram(a, b):
    dict_a = str_to_dict(a)
    dict_b = str_to_dict(b)

    if len(dict_a) == 0:
        return len(dict_b)

    if len(dict_b) == 0:
        return len(dict_a)

    count = 0
    for k in dict_a:
        if k not in dict_b:
            count += dict_a[k]
        else:
            count += abs(dict_a[k] - dict_b[k])
            dict_b[k] = -1

    for key, value in dict_b.items():
        if value != -1:
            count += value

    return count


a = 'cde'
b = 'abc'
print(make_anagram(a, b))
