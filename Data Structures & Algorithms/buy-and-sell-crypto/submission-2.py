class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # l = buy
        # r = sell
        l = 0
        r = 1
        while r < len(prices):
            prof = prices[r] - prices[l]
            res = max(res, prof)
            if prices[l] > prices[r]:
                l = r
            r += 1

        return res