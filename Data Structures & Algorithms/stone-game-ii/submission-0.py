class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        # return max alice
        def dfs(alice, i, m):
            if i == len(piles):
                return 0

            if (alice, i, m) in dp:
                return dp[(alice, i, m)]

            res = 0 if alice else float("inf")
            total = 0

            for X in range(1, 2 * m + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(m, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(m, X)))
            dp[(alice, i, m)] = res
            return res

        return dfs(True, 0, 1)

