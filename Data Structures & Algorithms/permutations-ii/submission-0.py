class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        counts = {n : 0 for n in nums}
        for n in nums:
            counts[n] += 1

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1

                    backtrack()
                    counts[n] += 1
                    perm.pop()

        backtrack()
        return res

        