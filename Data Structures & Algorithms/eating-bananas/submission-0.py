class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # len(p) <= h
        # k = 1......max(piles) <- solution one of these
            # binary search
        res = max(piles)

        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
