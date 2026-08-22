class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # (l, r) -> max amount ALICE can get

        # retrun the MAX AMOUNT ALICE can get, NOT BOB
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            # this is how you check who's turn it is
            even = True if (r - l) % 2 else False

            # if it is bob's turn it will be 0
            # this is because this function is for finding how much alice gets
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > sum(piles) // 2

        
            

