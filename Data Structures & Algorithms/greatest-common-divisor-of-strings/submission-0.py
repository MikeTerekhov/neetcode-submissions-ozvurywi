class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # L1 mod sub must == 0
        # L2 mod sub must == 0
        # greedy try longest version and keep making smaller until it fits in both strings
        l1, l2 = len(str1), len(str2)

        def isDivisor(l):
            # check that the sub fits in both
            if l1 % l and l2 % l: return False
            # check multiplying sub to get original back
            f1, f2 = l1 // l, l2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(l1, l1), 0, -1):
            if isDivisor(l): return str1[:l]
        return ""