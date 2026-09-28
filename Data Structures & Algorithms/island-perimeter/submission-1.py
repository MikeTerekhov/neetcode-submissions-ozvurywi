class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))
            p = dfs(r + 1, c)
            p += dfs(r - 1, c)
            p += dfs(r, c + 1)
            p += dfs(r, c - 1)    
            return p

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:    
                    return dfs(i, j)