class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # know have n edges and n nodes
            # becuase told when +1 edge we have exactly 1 cycle
                # no redundant edges

        N = len(edges)
        # initially each node is its own parent
        # [0 1 2 3 4 ...]
        par = [i for i in range(N + 1)]
        # rank of each node (initially all 1)
        rank = [1] * (N + 1)

        # find parent of a node
        def find(curr):
            # look at parent of curr
            # if not itself then must recursively go up the chain to find parent
            if curr != par[curr]:
                par[curr] = find(par[curr])
            return par[curr]
        
        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2:
                return False

            # make p2 a child of p1
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2): return [n1, n2]