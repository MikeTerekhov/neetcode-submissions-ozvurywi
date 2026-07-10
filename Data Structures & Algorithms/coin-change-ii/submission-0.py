class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # caching
        # decision tree of which coin we choose
        # how to make paths distinct? 
            # make paths only take all coins excpet one to paths unique
        
        # index i on which coin we are on
        # O(mn)

        # dp solutions
        # 2-D
        # x - amount (0 -> amount)
        # y - value of coins
        # base case -> 1 way to make 0 amount
        # bottom up 
        # look to the right and below
        # look 'coin amount' to the right or directly below
            # put the sum of the two
            # this is because we want all possibilities!
        
        # O(n) memory
        # if we fill up grid in diff order can save memory
        dp = [0] * (amount + 1)
        # 1 way to make total of 0 base base
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]

            dp = nextDP

        return dp[amount]









