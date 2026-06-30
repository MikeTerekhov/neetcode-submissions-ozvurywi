class Solution:
    def rob(self, nums: List[int]) -> int:
        # run house robber 1 on 
            # everything but first element
            # everything but last element
                # take max

        # edge case 1 and only house 
            # add nums[0] in max
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            # 'newRob' is like a temp
            # rob2 is the best you can do through the current house
            # rob1 is the best through the house two back. 
            # newRob = max(rob1 + n, rob2) is the choice to either rob this house (add n to the two-back total) or skip it (carry rob2 forward). 
            # The two assignments then shift the window forward by one.
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2