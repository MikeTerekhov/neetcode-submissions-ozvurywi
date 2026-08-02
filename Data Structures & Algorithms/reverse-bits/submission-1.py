class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # this just gets the right-most bit
            # ith bit of n
            # & 1 gets you that bit
            bit = (n >> i) & 1
            # update in reverse order, star in largest go to smallest
            res = res | (bit << (31 - i))

        return res