class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # # 1 way to sum to 0 with the first 0 elements
        # dp[0][0] = 1

        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i + 1][curr_sum + nums[i]] += count
        #         dp[i + 1][curr_sum - nums[i]] += count

        # return dp[len(nums)][target]

        # CUR_SUM -> COUNT
        dp = defaultdict(int)

        # 1 way to sum to 0 with the first 0 elements
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]