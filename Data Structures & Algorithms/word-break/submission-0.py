class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # base case
            # 'empty word' technically in dictionary
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (
                    # can we even fit the word we are considering?
                    (i + len(word)) <= len(s) and
                    # do we have a match?
                    s[i : i + len(word)] == word 
                ):
                    # recurence relation
                    dp[i] = dp[i + len(word)]

                # do not need to continue looping through words if found a way to break
                if dp[i]: break

        return dp[0]