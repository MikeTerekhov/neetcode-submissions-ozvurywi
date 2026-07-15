class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # brute force -> decision tree
        # this is too inefficient
        # need dp
        # subproblems:
            # pick a value and say that 'we will pop it last'-> i pointer
            # 2d dp table with a left and right pointer
            # keep the value we saved for last in place and use as 'implicit boundary'
                # [val * l ptr * r ptr] + dp[left subarray] + dp[right subarray]

        # time -> O(n^3) -> find subarrays -> n^2 and then iterate so mult by another n

        # pad for edge cases
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                # [val * l ptr * r ptr] + dp[left subarray] + dp[right subarray]
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
            
        # -2 to account for the padding
        return dfs(1, len(nums) - 2)