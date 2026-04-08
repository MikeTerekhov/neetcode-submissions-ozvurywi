class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            print("mid" , nums[m])
            print("l", nums[l])
            print("r", nums[r])
            print("-----------------")
            # mid is less than target
                # answer in right portion of array
            if nums[m] < target:
                l = m + 1
                print("less")
            # mid is greater than target
                # answer in left portion of array
            elif nums[m] > target:
                r = m - 1
                print("greater")
            else:
                return m
        
        return -1