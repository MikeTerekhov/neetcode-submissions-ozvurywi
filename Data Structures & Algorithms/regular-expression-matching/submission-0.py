class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # . -> matches any character
        # * repeats previous element any amount of times
        # .* -> . , .. , .., etc
        # i indput index
        # j pattern index
        # decision tree -> O(2^n) -> implement cache - ing
        # * -> j + 2 if we do not take an element
        # match a letter -> increment i
            # leave j there just in case we can repeat with a *

        # perfect match -> i and j are OUT OF BOUNDS
        # j >= len(pattern) and i not out of bounds -> FALSE
        # i >= len(input) and j still in bounds  -> can still be true
        
        # TOP DOWN memoization

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            # check if there is a match
                # first make sure i in bounds
                # chars actually equal
                # . in prefix allows for any char to work as match
            match = (i < len(s)) and ((s[i] == p[j]) or (p[j] == '.'))
            # check for the * char
                # make sure j in bounds
            if ((j + 1) < len(p)) and p[j + 1] == '*':
                # 2 options when encounter *
                    # NO use * -> dfs(i, j + 2)
                    # use * -> (match and dfs(i + 1, j))
                        # NOTE for us to use the *, we must make sure chars match hence using the match var from above
                cache[(i, j)] = (
                    dfs(i, j + 2) or (match and dfs(i + 1, j))
                )
                return cache[(i, j)]
            # simple match no nonsense with *
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            # only path left is just no match
            cache[(i, j)] = False
            return False

        return dfs(0, 0)



