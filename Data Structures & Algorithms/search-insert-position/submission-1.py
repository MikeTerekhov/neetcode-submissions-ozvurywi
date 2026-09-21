class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # ans : 1
        # [1, 3, 4]
        # 0 1 2
        # target : 2
        # m = 3
        # l = 0
        # r = 0
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l 
            