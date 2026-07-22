class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute force -> explore every path O(n^n)
            # can cache -> O(n^2)

        # greedy -> O(n)
        # shift goal post backwards from end
        # iterate in reverse

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0