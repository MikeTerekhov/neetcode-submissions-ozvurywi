class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # indicies
        slow = 0
        fast = 0

        while True:
            # advance slow and fast ptrs

            # by 1
            slow = nums[slow]
            # by 2
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        # round two wait for them to equal same one
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow