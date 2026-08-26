class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # decision tree
        # cache repeated work
            # key is the remaining amount needed to get to target
        
        # bottom up DP
            # want DP[4]
            # DP[0] = 1 base base
            # vals are the nums in nums
            # dp[4] = dp[4-val1] + dp[4-val2] .....

        # DP[0] = 1 base base
        # 1 way to get 0 because all positive vals
        dp = { 0 : 1 }

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                # if total - n is negative, just return 0
                dp[total] += dp.get(total - n, 0)

        return dp[target]