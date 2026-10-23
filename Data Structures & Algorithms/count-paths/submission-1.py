class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            next_row = [1] * n
            for j in range(n - 2, -1, -1):
                # look 1 below and 1 to the right
                next_row[j] = next_row[j + 1] + row[j]

            row = next_row

        return row[0]