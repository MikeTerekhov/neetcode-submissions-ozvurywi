class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            # n % 2 determines whether last digit is 0 or 1
                # n % 2 = 1 when ends with 1
                # n % 2 = 0 when ends with 0
            res += n % 2
            # this 'removes last bit', same as n / 2
            n = n >> 1
        return res