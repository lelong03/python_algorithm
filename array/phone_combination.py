class Solution(object):
    CHAR_DICT = {
        '0': [' '],
        '1': [''],
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_len = len(digits)
        result = []
        for i in range(digits_len):
            c = digits[i]
            if c not in self.CHAR_DICT:
                continue
            if result == []:
                result += self.CHAR_DICT[c]
            else:
                temp = []
                for s in result:
                    for p in self.CHAR_DICT[c]:
                        temp.append("%s%s" % (s, p))
                result = temp
        return result


print Solution().letterCombinations("23")
