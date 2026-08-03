class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR
        # any number XOR with 0 -> that number
        # x XOR x -> 0 always
        # order does not matter
        # range array XOR with given array -> missing number
        # subtract sum(range) - num(input)

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res
