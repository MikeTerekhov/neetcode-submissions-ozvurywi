class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the queries and intervals
        # iterate from left to right
        # min heap -> keep track of intervals it is a part of
        # (size, right value)
        # size = right - left + 1
        # time : O(nlogn + qlogq) -> iterate + sort
        # use hash map to mantain order for output
        # is val <= left value? -> yes -> add to min heap
        # use min heap to find smallest val in O(1)
        # must remove all invalid intervals per val
            # compare right val
            # while right val < query : pop

        intervals.sort()
        minHeap = []
        # i is an intervals iterator
        res, i = {}, 0
        for q in sorted(queries):
            # we are in bounds and query within range
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i][0], intervals[i][1]
                heapq.heappush(minHeap, (right - left + 1, right))
                i += 1

            # must remove all invalid intervals per val
                # compare right val
                # while right val < query : pop
                # minHeap[0] -> smallest val
                    # [1] is the right value of smallest intervals
                    # and we check if query falls within the range
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # -1 if query not a part of intervals
            res[q] = minHeap[0][0] if minHeap else -1

        return [ res[q] for q in queries]
