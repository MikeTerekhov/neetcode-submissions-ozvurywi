class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # modified dijkstras
        # O(n^2logn)
        # minHeap -> frontier -> (max h, r, c) -> max(curr, prevheight)
        # target bottom right
        # want to minimize max height
        # visit hashset
        # init : minheap([0, r, c])
            # pop
            # go thru neighbors

        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]] # (max h, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while minH:
            maxH, r, c = heapq.heappop(minH)
            #visit.add((r, c))
            
            if r == N - 1 and c == N - 1:
                return maxH

            # loop through dirs
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                # out of bounds or in visit
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue
                
                visit.add((neiR, neiC))
                # this is what we really care about
                newMaxH = max(maxH, grid[neiR][neiC])
                heapq.heappush(minH, [newMaxH, neiR, neiC])

            

            