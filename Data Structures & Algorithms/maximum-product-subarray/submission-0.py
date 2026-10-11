class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minS = 1
        maxS = 1

        res = max(nums)

        # reset max and min to 1 for 0

        for n in nums:
            if n == 0:
                minS = 1
                maxS = 1
                continue
            else:
                tmp = minS * n
                minS = min(n, minS * n, maxS * n)
                maxS = max(n, tmp, maxS * n)
                res = max(res, maxS)

        return res