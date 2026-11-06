class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        res = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        # stack contains all rotten
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
            res += 1

        return res if fresh == 0 else -1
                