class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        j = 0
        c = 1

        while True:
            if i == len(word1) and j == len(word2):
                break
            if c % 2 and i < len(word1):
                res += word1[i]
                i += 1
            elif j < len(word2):
                res += word2[j]
                j += 1
            c += 1

        return res