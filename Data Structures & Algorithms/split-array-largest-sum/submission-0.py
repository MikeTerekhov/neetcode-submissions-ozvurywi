class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search
        # lowest : max(nums)
        # highest : sum(nums)
        # bin search to get new highest which is the ans
        # function to check if can split into m groups with middle bound

        l = max(nums)
        r = sum(nums)

        res = r

        def canSplit(largest):
            subArr = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    # make new group
                    subArr += 1
                    curSum = n
            return subArr + 1 <= k

        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res





