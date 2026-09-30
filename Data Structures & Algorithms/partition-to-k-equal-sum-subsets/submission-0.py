class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        used = [False] * len(nums)

        # k = subsets needed left
        def backtrack(i, k, subSetSum):
            if k == 0:
                return True
            if subSetSum == target:
                # start at the beginning again
                # finding new subset
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or subSetSum + nums[j] > target:
                    continue
                used[j] = True

                if backtrack(j + 1, k, subSetSum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, k, 0)