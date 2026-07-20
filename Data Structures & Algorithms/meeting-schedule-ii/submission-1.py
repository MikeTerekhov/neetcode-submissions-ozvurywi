"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0
        res = 0
        # pointers to iterate over SORTED start and end arrays
        s, e = 0, 0

        while s < len(intervals):
            # this is the case that a meeting overlaps and starts before meeting ends
            # increment start
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                # no overlap
                e += 1
                count -= 1
            
            res = max(res, count)

        return res