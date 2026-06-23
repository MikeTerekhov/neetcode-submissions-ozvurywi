class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    # if out of bounds OR not encounter a FRESH ORANGE -> do nothing
                    if nr == ROWS or nc == COLS or nr < 0 or nc < 0 or grid[nr][nc] != 1 :
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append([nr, nc])
            time += 1

        return time if fresh == 0 else -1
                