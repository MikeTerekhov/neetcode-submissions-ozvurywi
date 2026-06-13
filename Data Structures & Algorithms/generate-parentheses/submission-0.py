class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openCount, closedCount):
            # valid IFF openCount == closedCount == n
            if openCount == closedCount == n:
                res.append("".join(stack))
                return

            # only add open when openCount < n
            if openCount < n:
                stack.append("(")
                dfs(openCount + 1, closedCount)
                stack.pop()


            # only add closing when closedCount < openCount
                # more opens than closed so need 2 balance them
            if closedCount < openCount:
                stack.append(")")
                dfs(openCount, closedCount + 1)
                stack.pop()

        dfs(0, 0)
        return res