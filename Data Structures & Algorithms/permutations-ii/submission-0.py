class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {n : 0 for n in nums}
        for n in nums:
            counts[n] += 1
        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())

            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1

                    dfs()

                    counts[n] += 1
                    perm.pop()
            return res

        return dfs()