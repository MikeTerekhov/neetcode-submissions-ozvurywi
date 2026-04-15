class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0

        l = 0

        for r in range(len(s)):
            # increment count of char at right pointer
            counts[s[r]] = 1 + counts.get(s[r], 0)

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res