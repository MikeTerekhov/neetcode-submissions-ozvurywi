class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # count number of cards per value, b/c can have dupes
        # start with smallest value
            # see if we can use it to make group starting at that val
            # make sure array is divisible by group size
            # if make group decrement counts
            # always start at smallest value
            # min heap ! -> working with minimums
                # pop if count to 0
            # O(nlogn)

            # count to 0 -> pop
                # what if it is not the min?
                # use a tree map
                # NO NEED! because then we know we cant make the group!
                # this creates a 'hole'

        if len(hand) % groupSize != 0: return False

        # count = Counter(hand)
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                # count to 0 -> pop
                if count[i] == 0:
                    # NO NEED! because then we know we cant make the group!
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True






