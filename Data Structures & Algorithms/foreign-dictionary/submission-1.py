class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # topological sort
        # DAG
        # cycle -> invalid -> return ""
            # currently being visited path
        # must fo post order DFS (add @ end) then return with .reverse()
        # time -> # of characters

        # build adj list
        adj = { c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # funky base case: a is a prefix of b and a.length < b.length.
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # building adj list
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False -> visited, True -> in current path
        res = [] # remember to join and reverse when return

        def dfs(c):
            if c in visit:
                # this returns either true of false
                    # False -> visited so everything still chill we just already went to this node
                    # True -> node is actually in our current path right now so its a cycle -> return and res must be ""
                return visit[c]

            # signifies in current path
            visit[c] = True

            for nei in adj[c]:
                # this mean cycle
                if dfs(nei): return True

            # right before return to signify that path is over
            visit[c] = False
            res.append(c)

        for c in adj:
            # remember the True case above signifying we caught a cycle
            if dfs(c): 
                return ""

        res.reverse()
        return "".join(res)


