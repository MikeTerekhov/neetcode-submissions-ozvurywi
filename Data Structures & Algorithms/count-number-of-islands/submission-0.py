class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and grid[r][c] == "1"):
                    bfs(r, c)
                    islands += 1
            
        return islands