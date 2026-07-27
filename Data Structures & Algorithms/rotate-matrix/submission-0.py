class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        NUM_ROWS = len(matrix)

        for r in range(NUM_ROWS):
            for c in range(r, NUM_ROWS):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        for r in matrix:
            r.reverse()