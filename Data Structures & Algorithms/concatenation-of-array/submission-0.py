class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_to_add = 2 * len(nums)
        i = 0
        ans = []
        j = 0
        # [2,2]
        # [2, 2, 2, 2]
        # n = 2 -> 4

        while True:
            if i == nums_to_add:
                break
            if j == len(nums):
                j = 0

            ans.append(nums[j])
            i += 1
            j += 1

        return ans