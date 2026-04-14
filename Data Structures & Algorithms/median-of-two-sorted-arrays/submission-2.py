class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # log(min(m, n))
            # running binary search on the shorter of the two

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # make sure A is always the shorter one
        if len(B) < len(A):
            A, B = B, A

        # bin search on shorter arr
        l = 0
        r = len(A) - 1
        while True:
            i = (l + r) // 2 # mid of A
            j = half - i - 2 # mid of B (-2 because on indexes, 1 for i and another for half calc above)

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # partition is not correct
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
