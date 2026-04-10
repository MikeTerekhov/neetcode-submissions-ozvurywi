class Solution:
    def findMin(self, nums: List[int]) -> int:

        # nums[m] >= nums[l]
        # [3, 4, 5, 1, 2]
        #  ^l    ^m

        n = len(nums)
        l = 0
        r = n - 1
        res = nums[0]

        while l <= r:
            # array already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # check mid
            m = (l + r) // 2
            res = min(res, nums[m])
            # want to search right part of array
            if nums[m] >= nums[l]:
                l = m + 1
            # want to search left part of array
            else:
                r = m - 1

        return res