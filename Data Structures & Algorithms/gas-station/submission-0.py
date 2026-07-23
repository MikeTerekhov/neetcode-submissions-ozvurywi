class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sum gas >= sum cost
        # DIFFERENCE ARRAY = gas - cost
        # iterate diff array and have a total var
            # if total becomes -
                # NOT start postition
                # reset total to 0
                # move on to the next starting position
                # O(n)

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            dif = (gas[i] - cost[i])
            total += dif
            if total < 0:
                total = 0
                res = i + 1

        return res