class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for cur, pre in prerequisites:
            adj[cur].append(pre)

        path = set()
        visit = set()
        res = []

        # dfs at everynode
        # add to output at end if no pre reqs

        def dfs(crs):
            if crs in path:
                return False

            if crs in visit:
                return True

            path.add(crs)
            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False

            path.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res


            