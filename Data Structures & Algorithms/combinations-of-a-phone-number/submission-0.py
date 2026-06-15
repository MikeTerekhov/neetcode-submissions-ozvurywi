class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i, curStr):
            # base case len translation == len input
            if len(digits) == len(curStr):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)

        if digits:
            dfs(0, "")

        return res