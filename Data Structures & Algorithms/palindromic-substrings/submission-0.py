class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for c in range(len(s)):
            # odd len subs
            l = c
            r = c
            while r < len(s) and l >= 0 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even len subs
            l = c
            r = c + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res