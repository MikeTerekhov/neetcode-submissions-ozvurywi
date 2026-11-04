class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstras
            # BFS min heap
            # key is max height we encountered along the way
            # along each path, keep track of max along the way

        minH = []
        visit = set()

        ROW, COL = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # add the initial square
        heapq.heappush(minH, [grid[0][0], 0, 0])
        visit.add((0, 0))

        while minH:
            height, r, c = heapq.heappop(minH)
            if r == ROW - 1 and c == COL - 1:
                return height
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if (nr, nc) in visit or nr < 0 or nc < 0 or nr == ROW or nc == COL:
                    continue

                newHeight = max(height, grid[nr][nc])
                visit.add((nr, nc))
                heapq.heappush(minH, [newHeight, nr, nc])

        
