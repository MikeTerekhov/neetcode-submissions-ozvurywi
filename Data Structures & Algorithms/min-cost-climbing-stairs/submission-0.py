class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n)
        # work backwards
        # 2 variables at a time

        # want to get here, so after array
        cost.append(0)

        # work backwards
        for i in range(len(cost) - 3, -1, -1):
            # two options : 1 step or two
            # want the minimum
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])