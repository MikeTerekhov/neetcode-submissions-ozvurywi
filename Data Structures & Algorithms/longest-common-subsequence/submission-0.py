class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # subproblems
            # abcde
            # ace
                # 1 + (dbce & ce)

            # bbcde
            # ace
                # (bbcde & ce) : exclude from first
                # (bcde & ace) : exclude from second

        # 2d grd
        # rows :  first string
        # cols :  second string
        # answer at top right [0][0] : bottom up dp
        # if chars equal ->  go diag since excluding chars from BOTH strings
        # go bottom or right depending on which string we steal a char from
            # check right or down and take the MAX of those 2
        # out of bounds default = 0
        # pad rows and cols with 0 

        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # matching case go diag
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

        # time : O(len(text1) * len(text2))


