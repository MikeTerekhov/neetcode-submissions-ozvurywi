class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s ptr
        i = 0
        # t ptr
        j = 0

        while j < len(t):
            if i >= len(s) - 1:
                return True
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return False