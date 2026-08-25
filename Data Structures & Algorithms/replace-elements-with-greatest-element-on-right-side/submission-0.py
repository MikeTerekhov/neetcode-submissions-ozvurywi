class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        prev = arr[n]
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = prev
            prev = max(prev, curr)

        arr[n] = -1
        return arr
