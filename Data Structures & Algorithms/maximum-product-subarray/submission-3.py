class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax  = 1, 1
        # Need cur min swolely for the computation of curMax because largest negative value multiplies by another negative vale creates positive

        for n in nums:
            # if see 0 just rest curmin and curmax to 1
            # if n == 0:
            #     curMin, curMax = 1, 1
            #     continue

            temp = curMax * n
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(curMin * n, temp, n)
            res = max(res, curMax)

        return res
