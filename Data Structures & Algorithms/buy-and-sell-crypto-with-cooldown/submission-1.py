class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # decision tree
            # buy, sell, cooldown
            # cache - index in prices array, boolean -> buy or sell
                # O(n)

        # state -> buy or sell?
        # if buy -> i + 1
        # if sell -> i + 2

        dp = {} # key = (i, buying) val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp: return dp[(i, buying)]

            if buying:
                # calculate price after buying
                buy = dfs(i + 1, not buying) - prices[i]
                #same cooldown
                cooldown = dfs(i + 1, buying)
                # cache in (i, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # calculate price after selling
                sell = dfs(i + 2, not buying) + prices[i]
                # same cooldown
                cooldown = dfs(i + 1, buying)
                # cache in (i, buying)
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]

        return dfs(0, True)
