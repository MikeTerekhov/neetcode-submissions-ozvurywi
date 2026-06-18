class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first == second:
                continue
            # first > second
                # -first - - second
            new_stone = (-first) + (second)
            heapq.heappush(stones, -new_stone)

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0