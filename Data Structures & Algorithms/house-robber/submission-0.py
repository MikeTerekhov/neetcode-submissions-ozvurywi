class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob  = max(arr[0] + rob[2:n], rob[1:n])
        # must solve subproblems
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            # cannot take adj!
            rob1 = rob2
            rob2 = temp

        # want to return the last val because thats when we get max for the whole arr
        return rob2