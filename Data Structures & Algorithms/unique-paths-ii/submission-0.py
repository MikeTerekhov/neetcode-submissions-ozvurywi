class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # only move to 0s
        # brute force -> DP
        # add total paths from surrounding openings
            # recurse to find these
        # BASE CASE : 1 way @ destination
        # add bottom + right to find solution in grid
            # fill in starting at dest then go left and up
                # bottom up 2d dp
                # do not need whole grid - reduce O(m*n) to O(n (size of row))

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        # this is the base case of "bottom right" destination
        dp[N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                # obstacle
                if obstacleGrid[r][c]:
                    dp[c] = 0
                # add below + to right
                # check not out of bounds for right value
                # bottom val will never go out of bounds since we just copying it using a single row of mem
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
                # if right val out of bounds, we just adding 0
                # NOTE : do not need this just showing the logic
                else:
                    dp[c] = dp[c] + 0

        return dp[0]
                
