class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums) // 2

        for c in counts:
            if counts[c] > n:
                return c