class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # look to the bottom and to the right
        # sum those up
        # do not need whole m*n memory
            # only need 2 rows

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[-1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c +  1 < cols:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]
