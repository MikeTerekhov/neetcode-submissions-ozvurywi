class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # JFK is the starting edge
        # DFS
        # adj list

        # need adj list to be sorted
            # so can return in lex order

        # finish condition len(result) == number of tickets + 1

        # might have to backtrack if we get stuck at a node with no back edge

        # O(v + e) but might backtrack -> O(E^2) , O(E) mem complexity 
        adj = { src : [] for src, dst in tickets }
        tickets.sort() # auto sorts by first letter
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1: return True
            if src not in adj: return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                # CAUTION must modify as we iterate so iterate over a copy (temp)
                adj[src].pop(i)
                res.append(v)

                if dfs(v): return True

                # got stuck!
                # must undo last decision 
                    # add i, v back in
                    # revert res
                adj[src].insert(i, v)
                res.pop()

            return False

        dfs("JFK")
        return res

