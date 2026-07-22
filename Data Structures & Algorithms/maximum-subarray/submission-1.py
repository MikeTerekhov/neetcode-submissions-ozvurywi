class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force ->  calc each sub arr -> O(n^3)
            # cache -> O(n^2)

        # can do better -> O(n)
        # iterate and keep track of curSum and a prefix amount
        # reset prefix if goes negative

        curSum = 0
        res = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(res, curSum)

        return res

