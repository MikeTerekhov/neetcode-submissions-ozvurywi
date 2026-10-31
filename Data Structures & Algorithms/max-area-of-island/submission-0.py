class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        res  = 0

        def dfs(r, c):
            if (
                (r, c) in visit or
                r == ROWS or
                c == COLS or 
                r < 0 or
                c < 0 or
                grid[r][c] == 0
            ):
                return 0
            visit.add((r, c))

            return (1 + dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))


        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
                
        return res
