class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        # this returns stones Alice gets
        # if alice -> max
        # if bob -> min
        def dfs(alice, i, m):
            if i == len(piles):
                return 0
            if (alice, i, m) in dp:
                return dp[(alice, i, m)]

            # since want to min bobs score, need to assign a big val so min() works
            res = 0 if alice else float("inf")
            # this is instead of nested for loop iterating through all possible 1...m piles
            total = 0
            for X in range(1, 2 * m + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                # alice turn
                if alice:
                    # note adding to total dfs call
                    res = max(res, total + dfs(not alice, i + X, max(m, X)))
                # bob turn
                else:
                    # note in bob's case we are not adding total
                    res = min(res, dfs(not alice, i + X, max(m, X)))

            dp[(alice, i, m)] = res
            return res

        return dfs(True, 0, 1)
