class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # go through s and t
        # if s[i] == t[j]
            # i + 1, j + 1
            # i + 1, j    <--- this is to find other matches
        # else
            # i + 1, j

        # 'a' and '' -> return 1
        # '' and '' -> return 1
        # '' and 'a' -> return 0, cannot make any

        cache = {}
        
        def dfs(i, j):
            # get to the end of second string so done
            if j == len(t):
                return 1
            # end of first string, no match
            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)
