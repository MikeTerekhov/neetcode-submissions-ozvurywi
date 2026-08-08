class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursion
        # divide and conquor
        # 2^10 = 2^5*2^5
        # x^-n = 1/x^n
            # take care of this at the end

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            # NOTE : odd n case must add the extra n
                # x^5 = x^2 * x^2 * x
            res = helper(x * x, n // 2)
            return x * res if n % 2 else res 

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

