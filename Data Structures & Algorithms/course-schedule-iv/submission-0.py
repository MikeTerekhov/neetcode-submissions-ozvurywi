class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # O(n^3), an n for merging sets as we pop up
        # DFS
        # as we pop up return the dependencies
        # for each course build the prereq list
            # this makes it faster to check
            # use a set

        # build pre-req list
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        # goal of this is to populate prereqMap
        def dfs(crs):
            if crs in prereqMap: 
                return prereqMap[crs]
            prereqMap[crs] = set()
            for p in adj[crs]:
                prereqMap[crs] |= dfs(p) # this is union, so just joining all the prereqs into the set that is denoted by prereqMap[crs]
                prereqMap[crs].add(p) 
            return prereqMap[crs]

        prereqMap = {} # map crs -> hashset of indirect prereq
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])

        return res

        