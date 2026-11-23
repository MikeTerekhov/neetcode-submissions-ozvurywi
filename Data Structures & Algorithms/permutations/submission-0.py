class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subprob = self.permute(nums[1:])
        res = []

        for p in subprob:
            for i in range(len(p) + 1):
                pc = p.copy()
                pc.insert(i, nums[0])
                res.append(pc)

        return res