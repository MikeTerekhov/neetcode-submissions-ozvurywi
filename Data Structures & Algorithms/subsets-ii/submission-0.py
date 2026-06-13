class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(subset, i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # take nums[i]
            subset.append(nums[i])
            dfs(subset, i + 1)

            subset.pop()
            # skip ALL occurences of nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(subset, i + 1)

        dfs([], 0)
        return res
            