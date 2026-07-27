class Solution:
    def checkValidString(self, s: str) -> bool:
        # can do dp with memoization but thats O(n^3)
        # instead this is O(n) time and O(1) space
        # keep two vars to keep track of the min and max number of left parentheses
        # reset lMin to 0 if it becomes -
        # if lMax become - then auto return FALSE

        lMin, lMax = 0, 0

        for c in s:
            if c == "(":
                lMin, lMax = lMin + 1, lMax + 1
            elif c == ")":
                lMin, lMax = lMin - 1, lMax - 1
            # wild card case *, so an option if a left or a right or nothing
            else:
                lMin, lMax = lMin - 1, lMax + 1
            if lMax < 0:
                return False
            if lMin < 0:
                lMin = 0

        return lMin == 0