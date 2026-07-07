class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # work backward
        # LIS[i] -> longest inc sub starting at index i
        # base-case -> LIS[len(nums)] = 1
        # if nums of index[i + 1] > index[i] then can add 1 to include that val
        # O(n^2) -> at each element loop thru every other element

        # fill in with 1 because that is the base case
        LIS = [1] * len(nums)

        # loop backward
        for i in range(len(nums) - 1, -1, -1):
            # loop thru all vals from i to the end
            for j in range(i + 1, len(nums)):
                # see if increasing
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)
