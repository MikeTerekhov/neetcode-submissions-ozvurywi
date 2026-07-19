class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # want to iterate in sorted order by start date
            # same start or start 2 before start 1
            # start 2 before 1 end
        # O(nlongn)

        # delete one with larger end value!

        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # no overlap!
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                # delete one with larger end value!
                # aka keep the MIN
                prevEnd = min(end, prevEnd)

        return res