class Solution:
    def tribonacci(self, n: int) -> int:  

        def fib(it, a, b, c):
            if it == n:
                return a
            return fib(it + 1, b, c, a + b + c)

        return fib(0, 0, 1, 1)
        