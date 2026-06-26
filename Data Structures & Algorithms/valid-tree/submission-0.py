class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # len visit set == num nodes
        # DFS visit paths
        if not n: return True

        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(cur, prev):
            if cur in visit:
                return False
            
            visit.add(cur)
            # loop thru neighbors
            for i in adj[cur]:
                if i == prev: continue
                if not dfs(i, cur): return False
            return True

        # default prev -1 because no nodes will have that val
        # and checks that no disconnected components
        return dfs(0, -1) and len(visit) == n 
