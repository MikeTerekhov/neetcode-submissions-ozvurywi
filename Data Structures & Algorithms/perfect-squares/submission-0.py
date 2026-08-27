class Solution:
    def numSquares(self, n: int) -> int:
        # bottom up
        # subproblems -> n - (perfect squares)
        # time : O(n * sqroot(n))
            # because we iterate bounded by root n
            # ex : 16 -> 4^2

        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                subproblem = target - square
                if subproblem < 0:
                    break
                # + 1 in the subproblem b/c we are "using a square" here
                dp[target] = min(dp[target], 1 + dp[subproblem])

        return dp[n]