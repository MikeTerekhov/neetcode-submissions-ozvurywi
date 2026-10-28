class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : [] for i  in range(numCourses)}
        path = set()

        for crc, pre in prerequisites:
            adj[crc].append(pre)

        def dfs(crs):
            if crs in path:
                return False
            if adj[crs] == []:
                return True

            path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False

            path.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True