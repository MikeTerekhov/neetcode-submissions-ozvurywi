class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = math.ceil(sum(stones) / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (sum(stones) - total))
            if (i, total) in dp:
                return dp[(i, total)] 

            res = min(dfs(i + 1, total),
            dfs(i + 1, total + stones[i]))
            dp[(i, total)] = res
            return res

        dp = {}
        return dfs(0, 0)