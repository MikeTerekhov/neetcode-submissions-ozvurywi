class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # edge case that interval BEFORE all other intervals
            # no overlap
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # insert after interval
            elif newInterval[0] > intervals[i][1]:
                # NOT appending new interval b/c dont know if overlap
                res.append(intervals[i])
            # must have overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res

