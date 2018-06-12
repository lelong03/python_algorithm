# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution(object):

    def update_dict(self, r_dict, ch):
        if ch in r_dict:
            r_dict[ch] += 1
        else:
            r_dict[ch] = 1
        return r_dict

    def create_dict_count(self, s):
        result = {}
        for c in s:
            self.update_dict(result, c)
        return result

    def update_dict_count(self, r_dict, str, i, j):
        if str[i] in r_dict:
            r_dict[str[i]] -= 1
        if r_dict[str[i]] == 0:
            del r_dict[str[i]]
        r_dict = self.update_dict(r_dict, str[j])
        return r_dict

    def checkInclusion(self, s1, s2):
        s1_len = len(s1)
        s1_dict_count = self.create_dict_count(s1)
        s2_len = len(s2)
        slide_window = {}
        for i in range(s2_len-s1_len+1):
            if i == 0:
                slide_window = self.create_dict_count(s2[i:s1_len])
            else:
                slide_window = self.update_dict_count(slide_window, s2, i-1, i+s1_len-1)
            if slide_window == s1_dict_count:
                return True
        return False

s1 = "df"
s2 = "afgcda"
print Solution().checkInclusion(s1, s2)