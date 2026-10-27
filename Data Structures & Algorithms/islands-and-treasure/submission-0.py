class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # BFS from all gates
        q = deque()
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return

            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                # add all gates to q
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1