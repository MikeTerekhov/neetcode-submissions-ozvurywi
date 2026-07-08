class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down or right moves ONLY
            # paths are eliminated as we move since cant go up or left

        # dp
            # cache[r][c] = number of ways to get to dest from (r, c)
            # add vals of R + D (right + down) to find each val
            # pad all outsides with 0
            # start from destination
            # answer at start position

        # whole bottom row is 1s
        # all right cols are 1
            # because they border 0s and 1 + 0 -> 1

        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                # right ->  newRow[j + 1]
                # down -> row[j]
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]
        # time : iterate through each grid space with a constant time operation -> O(rows*cols)
