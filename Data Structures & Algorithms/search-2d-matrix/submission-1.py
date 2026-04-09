class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top = 0
        bot = ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            # matrix[row][-1] is the right most element in that row
            if target > matrix[row][-1]:
                top = row + 1
            # NOTE : !!!
            # matrix[row][0] is the first element in that row
            elif target < matrix[row][0]:
                bot = row - 1
            # we are in the row that contains the target if it exists
            else:
                break
        # check for invalid condition after break
        if not (top <= bot): return False

        l = 0
        r = COLS - 1
        row = (top + bot) // 2

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else: return True

        return False


