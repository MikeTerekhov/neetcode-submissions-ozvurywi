class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # [3, 4, 5, 1, 2]

        # nums[l] <= nums[m] -> in left softed portion
        # else: in right sorted portion

        while l <= r:

            m = (l + r) // 2
            if target == nums[m]: return m

            # we are in left portion
            if nums[l] <= nums[m]:
                if target < nums[l]:
                    # search right
                    l = m + 1
                elif target > nums[m]:
                    # search right
                    l = m + 1
                else:
                    r = m - 1
            # we are in right portion
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
