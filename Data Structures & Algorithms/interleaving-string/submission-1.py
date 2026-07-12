class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # O(m*n)
        # i1 p to string 1
        # i2 p to string 2
        # i3 (resulting string) = i1 + i2
        # if both words have a matching letter
            # need decision tree to explore both paths
        # store true / false at each pointer combination

        # base case -> both pointers out of bounds
        # add an extra row and column to 2D dp grid
        # fill in base cases

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # both out of bound, bottom row, rightmost column
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # note i + j is index in the third string
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

