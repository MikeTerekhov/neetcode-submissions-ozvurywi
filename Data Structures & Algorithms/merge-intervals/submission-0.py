class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start value
            # O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # this gets the end position of last added interval
            lastEnd = output[-1][1]
            if start <= lastEnd:
                # [1, 5], [2, 4] = [1, 5]
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output