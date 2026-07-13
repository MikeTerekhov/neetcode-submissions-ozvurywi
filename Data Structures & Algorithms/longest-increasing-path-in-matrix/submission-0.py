class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS brute force already kinda caches repeated work
        # time and space -> O(m*n)
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {} # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if r == ROWS or c == COLS or r < 0 or c < 0 or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp: 
                return dp[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                # -1 is a good default val since all nums greater than 0
                dfs(r, c, -1)

        return max(dp.values())