class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # backtracking with cache solution
        # NOT DP
        # need a dp cache to make it time acceptable

        # dp = {} # maps to the number of ways

        # def backtrack(i, curr_sum):
        #     if (i, curr_sum) in dp:
        #         return dp[(i, curr_sum)]
        #
        #     if i >= len(nums):
        #         return 1 if curr_sum == target else 0
        #
        #     dp[(i, curr_sum)] = (
        #         backtrack(i + 1, curr_sum + nums[i]) +
        #         backtrack(i + 1, curr_sum - nums[i])
        #     )
        #
        #     return dp[(i, curr_sum)]

        # return backtrack(0, 0)

        # ----------------------------------------
        # 2D dp
        # bottom up
        # y = index of nums array
        # x = - max to + max
        # dp[i][cur_sum] = count of ways to do that
        # want dp[all nums][target]

        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # # base case
        # # 0 elements, 0 sum -> 1 way
        # dp[0][0] = 1
        #
        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i + 1][cur_sum + nums[i]] += count
        #         dp[i + 1][cur_sum - nums[i]] += count
        #
        # return dp[len(nums)][target]

        # MEMORY OPTIMIZED BY remembering only 1 row at a time
        dp = defaultdict(int)
        # base case
        # 0 elements, 0 sum -> 1 way
        dp[0] = 1

        for i in range(len(nums)):
            nextDP = defaultdict(int)
            for cur_sum, count in dp.items():
                nextDP[cur_sum + nums[i]] += count
                nextDP[cur_sum - nums[i]] += count
            dp = nextDP

        return dp[target]

