class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # (r + c)
        NegDiag = set() # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        # go row by row dfs
        def dfs(r):
            # base case is get to the last row
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in NegDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                NegDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)
                # clean up
                cols.remove(c)
                posDiag.remove(r + c)
                NegDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res

                