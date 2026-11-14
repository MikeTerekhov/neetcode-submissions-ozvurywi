class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # (l, r) -> max alice can have

        # return max alice total
        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            # who turn is it?
            alice = True if (r - l) % 2 else False
            left = piles[l] if alice else 0
            right = piles[r] if alice else 0
            if alice:
                res = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            else:
                res = min(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            dp[(l, r)] = res
            return res
        # score to beat is just sum / 2
        score_to_beat = sum(piles) // 2
        return dfs(0, len(piles) - 1) > score_to_beat
            