class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # min heap -> [endPos, numPas]
        minHeap = []
        curPass = 0

        # sort based on start pos of trip
        trips.sort(key = lambda t: t[1])

        for t in trips:
            numPass, start, end = t

            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)

            curPass += numPass
            if curPass > capacity:
                return False

            heapq.heappush(minHeap, [end, numPass])
        return True


