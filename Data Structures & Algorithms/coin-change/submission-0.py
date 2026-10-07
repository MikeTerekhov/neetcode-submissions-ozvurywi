class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        # base case 0 ways to get 0 dp[0] = 0
        dp[0] = 0

        # coins = [1, 2, 3]
        # amount = 5
        # 1, 2, 3, 4, 5
        # sol = 2 ( 2 + 3 )

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a - c] + 1, dp[a])

        if dp[amount] == amount + 1:  return -1
        else: return dp[amount]