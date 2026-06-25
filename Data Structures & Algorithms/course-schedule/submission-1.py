class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preMap
            # course -> prereq
        # DFS on the map
            # base case -> no prereq per course
        # O(nodes + prereq)
        # visit set to detect cycle
        preMap = { i :[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visit set stores all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            # this indicates a cycle / loop
            if crs in visitSet:
                return False
            # a course has no prereqs so its valid
            if preMap[crs] == []:
                return True
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            # IMPORTANT
                # "unwind" the visit set so this keeps track if we re see a node 
                # during a CURRENT DFS path not it total over throughout the whole algorithm
                # this is strictly for the current PATH
                # NOTICE this happens after all the dfs calls anove in the for loop right above so this is unwind
            visitSet.remove(crs)
            # this indicates this course can be completed since we verified it so no repeated work
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

