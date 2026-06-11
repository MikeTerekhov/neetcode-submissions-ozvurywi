class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        # SORT
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            if i >= len(candidates):
                return 

            # include cadidates[i]
                # NOTE : i + 1 -> NO reuse
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # skip cadidates[i]
            cur.pop()
            # skip duplicates
                # skip all instances of this
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res