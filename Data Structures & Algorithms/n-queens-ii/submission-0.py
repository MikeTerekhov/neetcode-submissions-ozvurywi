class Solution:
    def totalNQueens(self, n: int) -> int:
        # pos diag = (r + c)
        # neg diags = (r - c)
        col = set()
        posD = set()
        negD = set()

        res = 0

        def dfs(r):
            if r == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                if c in col or (r + c) in posD or (r - c) in negD:
                    continue
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                dfs(r + 1)
                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)

        dfs(0)
        return res