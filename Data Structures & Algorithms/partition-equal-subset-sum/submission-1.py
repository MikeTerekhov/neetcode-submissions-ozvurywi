class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force
            # include or not an element -> 2 ^ n
                # decision tree
                # over target -> end path
                # target = sum(array) / 2
            # caching -> subproblem with (target - num) new target
                # O(n * sum(nums) / 2)
        # DP
            # work backwards
            # go per element
                # make dp set and initialize with 0
                # add to a set all (nums[i] + each element already in dp set)
                    # careful -> modifying and iterating set 
                        # make clone
            # if set contains target -> return True

        if sum(nums) % 2: return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            # this is because we cant iterate and modify the set at same time
            # could also just dp.clone()
            nextDP = set()
            for t in dp:
                # early stoppage optimization
                if (nums[i] + t) == target: return True
                nextDP.add(nums[i] + t)
                nextDP.add(t)

            dp = nextDP

        return (target in dp)



            
