from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dummy solution
        # return sorted(s) == sorted(t)

        s_chars = dict(Counter(s))
        t_chars = dict(Counter(t))
        
        for char in s_chars:
            if s_chars.get(char) != t_chars.get(char, 0):
                return False
        for char in t_chars:
            if t_chars.get(char) != s_chars.get(char, 0):
                return False

        return True

