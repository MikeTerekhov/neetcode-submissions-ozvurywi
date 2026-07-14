class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # w1 = '' w2 = '' return 0 operations
        # w1 = 'abc w2 = '' return 3 deletes ---> len(non-empty) word
            # reverse works too
        # w1[i] == w2[j]: (nothing added to operation count)
            # (i + 1, j + 1) subproblem
        # else (adds a 1 to operation count)
            # insert -> i, j + 1 
            # delete -> i + 1, j
            # replace -> i + 1, j + 1

        # 2d dp grid
            # add an outer layer with the base cases
            # empty string -> 0
            # others -> len(string)
            # above are the directions in which we move in the grid
            # fill in bottom up

        cache = [ [float("-inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        #  THIS PART : w1 = 'abc w2 = '' return 3 deletes ---> len(non-empty) word
        # fill up bottom row
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        # fill up last col
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # w1[i] == w2[j]: (nothing added to operation count)
                # (i + 1, j + 1) subproblem
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    # 1+ is for the added operation count
                        # else (adds a 1 to operation count)
                        # insert -> i, j + 1 
                        # delete -> i + 1, j
                        # replace -> i + 1, j + 1
                    cache[i][j] = 1 + min(cache[i][j + 1], cache[i + 1][j], cache[i + 1][j + 1])

        return cache[0][0]









