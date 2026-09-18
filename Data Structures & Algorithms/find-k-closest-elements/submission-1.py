class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            # is including the point to the left or to the right better for window?
            if x - arr[m] > arr[m + k] - x:
                # right side of arr
                l = m + 1
            else:
                # left side of arr
                r = m

        return arr[l:l+k]