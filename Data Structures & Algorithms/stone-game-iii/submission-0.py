class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        
        # returning either (alice - bob) or (bob - alice)
        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]

            # need this because stoneValue can be negative
            res = float("-inf")
            # make sure grabbing 3 stones is not out of bounds
            for j in range(i, min(i + 3, len(stoneValue))):
                # returning the diff allows us to always do max
                res = max(res, sum(stoneValue[i : j + 1]) - dfs(j + 1))
            
            dp[i] = res
            return res

        return "Alice" if dfs(0) > 0 else ("Bob" if dfs(0) < 0 else "Tie")

            
