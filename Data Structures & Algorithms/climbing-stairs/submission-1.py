class Solution:
    def climbStairs(self, n: int) -> int:
        # last spot in dp array so 1 step
        one = 1
        # second to last spot in dp array so
        two = 1
        # 2 vars shifted n - 1 times

        # fib type vibe
            # work backwards to get answer starting from 0
        for i in range(n - 1):
            temp = one
            # way to get from position is sum of 'next' two
            one  = one + two
            two = temp

        # this is essentially returning dp[0]
        return one