class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijktras shortest path alg
        # min heap (path, node)
            # add node
            # pop it
                # add neighbors to minheap
                # keep track of WHOLE path not just prev edge
        # E = V^2 (most number of edges)
        # O(E*logV^2) -> O(E*logV)
        # disconnected node -> alg fails can't visit all so return -1
            # len visit == n ?

        # adjacency list
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # path cost of 0 to get to the starting node
        # note starting node is given to us -> k
        minHeap = [(0, k)]
        visit = set()
        res = 0
        while minHeap:
            # pop min
            cost_main, node_main = heapq.heappop(minHeap)
            if node_main in visit:
                continue
            visit.add(node_main)
            res = max(res, cost_main)

            # go through neighbors BFS
            for node_nei, cost_nei in edges[node_main]:
                if node_nei not in visit:
                    # NOTE : if node not visited we add to HEAP not cisit set, we do not visit neighbors just append to Q
                    # NOTE : cost is sum along path not just that cost_nei
                    heapq.heappush(minHeap, (cost_nei + cost_main, node_nei))

        return res if len(visit) == n else -1
                    
