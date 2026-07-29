class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum spanning trees

        # 1. make edges -> manhattan distance
        # 2. do prims alg MST
            # use min heap
            # n - 1 edges to connect everything with no cycles
            # start at a node
                # do BFS (add all neighbors to frontier)
                # visit hashset
                # frontier (minheap) -> (cost, node)
                # stop when number nodes == len(visit set)
                # pop from minheap, add to visit, work with neighbors of next element
                # note can add duplicates to frontier hence O(n^2logn)

        N = len(points)

        # BUILDING ADJ LIST

        adj = { i:[] for i in range(N) } # i : list of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2) # 'cost'
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prims alg
        res = 0
        visit = set()
        minH = [[0, 0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit: 
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [nei_cost, nei])

        return res


                

