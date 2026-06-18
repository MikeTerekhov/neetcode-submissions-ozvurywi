class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for p in points:
            x = p[0]
            y = p[1]

            dis = pow(x, 2) + pow(y, 2)
            res.append([dis, x, y])

        heapq.heapify(res)

        ret = []
        while k > 0:
            val = heapq.heappop(res)
            ret.append([val[1], val[2]])
            k -= 1
        
        return ret