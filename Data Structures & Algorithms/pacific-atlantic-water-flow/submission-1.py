class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # NOTE : since going from ocean to other cells, flip logic
            # water flows if heights == or INCREASE (opposite if start at cells and go to ocean)
            # heights[r][c] < prevHeight

        def dfs(r, c, visit, prevHeight):
            if (
            r < 0 or c < 0 or 
            r == ROWS or c == COLS or 
            (r, c) in visit or 
            (heights[r][c] < prevHeight)
            ):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # this iterates through the top and bottom rows that border the respective oceans
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # this iterates through the left and right cols that border the respective oceans
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
