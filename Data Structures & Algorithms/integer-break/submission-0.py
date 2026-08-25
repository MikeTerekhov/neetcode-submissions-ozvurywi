class Solution:
    def integerBreak(self, n: int) -> int:
        # base case, 1 -> 1
        dp = { 1 : 1 }

        for num in range(2, n + 1):
            # this is allowing us to not break up numbers if it is not target
            # ex : 3 do not make it into 2 and 1
                # example do not want to break 3 up like below into 2 and 1
                # 3 * 1 > 2 * 1 
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num -  i]
                dp[num] = max(dp[num], val)

        return dp[n]

        # NOTE : this is the recursive solution
        def dfs(num):
            if num in dp:
                return dp[num]
            # this is allowing us to not break up numbers if it is not target
            # ex : 3 do not make it into 2 and 1
                # example do not want to break 3 up like below into 2 and 1
                # 3 * 1 > 2 * 1 
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                f1 = dfs(i)
                f2 = dfs(num - i)
                val = f1 * f2
                dp[num] = max(dp[num], val)
            return dp[num]

        # return dfs(n)
