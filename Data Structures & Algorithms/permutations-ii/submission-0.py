class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # input array to a counts hashmap
        m = Counter(nums)
        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in m:
                if m[n] > 0:
                    perm.append(n)
                    m[n] -= 1

                    dfs()

                    m[n] += 1
                    perm.pop()

        dfs()
        return res
