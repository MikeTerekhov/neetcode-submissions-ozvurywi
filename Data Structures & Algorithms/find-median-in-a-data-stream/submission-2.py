class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # only min heaps supported 
        heapq.heappush(self.small, -1 * num)

        # check that all vals are smaller in small
        if self.small and self.large and (-1*self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # check lengths of heaps and make sure they do not differ by more than 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.large) < len(self.small):
            return -1 * self.small[0]
        
        return (self.large[0] + (-1 * self.small[0]))/2.0
        
        