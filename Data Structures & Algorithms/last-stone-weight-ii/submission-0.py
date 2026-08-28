class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # find 2 piles that are 1/2 total sum(stones)
        # bounded knapsack
        # do a tree -> include or not a stone
            # many paths (2^n)
            # caching -> (i, total)
            # time : n * sum(stones)

        stoneSum = sum(stones)
        half = stoneSum // 2
        dp = {}

        # 23 -> 12, 11
        def dfs(total, i):
            if i == len(stones) or total >= half:
                return abs(total - (stoneSum - total))
            if (total, i) in dp:
                return dp[(total, i)]

            dp[(total, i)] = min(dfs(total, i + 1), dfs(total + stones[i], i + 1))
            return dp[(total, i)]

        return dfs(0, 0)