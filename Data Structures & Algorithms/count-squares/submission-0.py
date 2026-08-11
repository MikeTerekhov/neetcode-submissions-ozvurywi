class CountSquares:

    def __init__(self):
        self.pCounts = defaultdict(int)
        self.lPoints = []

    def add(self, point: List[int]) -> None:
        self.pCounts[tuple(point)] += 1
        self.lPoints.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        # iterate over list of points
        for x, y in self.lPoints:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue

            res += self.pCounts[(x, py)] * self.pCounts[(px, y)]

        return res

