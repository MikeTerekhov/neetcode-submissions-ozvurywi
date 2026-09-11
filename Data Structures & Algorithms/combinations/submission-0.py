class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                # only use vals later in list since
                # [1, 2] == [2, 1]
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return res