class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # edge case : all values are negative
            # check if global max is > 0
                # return largest num in array
        # regular non circular:
            # curMax and globMax
        
        # for circular case 
            # also need a curMin and globMin
            # circularMax = sum(nums) - globMin
            # then do max(gobMax, circularMax) to get ans
                # essentially we are not including the smallest subarr from the center of the arr

        curMax = 0
        globMax = nums[0]
        curMin = 0
        globMin = nums[0]
        total = sum(nums)

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax




