class Solution:
    def jump(self, nums: List[int]) -> int:
        # always assume you can reach last index
        # levels
        # color code postitions we can get per number of jumps
        # BFS type
        # return number of color coded levels
        # determine bounds 
            # l = r + 1
            # r = max jump from prev section -> farthest variable per window

        # MAIN IDEA : simplified BFS

        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            # note : right bound inclusive
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res