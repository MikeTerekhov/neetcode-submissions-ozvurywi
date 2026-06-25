class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort
        # map node -> prereqs
        prereq = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # DFS until a course has no pres
            # add to output & cross out from map
            # pop back up

        # course has states:
            # visited -> added to output
            # visiting -> in DFS path, but not in output
                # cycle detection
            # unvisited -> not in output or DFS path
        output = []
        visit = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False: return []
        
        return output


        # cycle ->  return []
        # O(pres + courses) = O(v + E)
        # visitSet to determine cycle along DFS path