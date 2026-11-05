class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        minH = [] #[ path, node]
        heapq.heappush(minH, [0, k])

        visit = set()
        t = 0

        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(w1, t)

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, [w1 + w2, n2])

        return t if len(visit) == n else -1
