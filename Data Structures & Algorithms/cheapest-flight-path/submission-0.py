class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford
            # BFS
            # k stops -> k + 1 layers of BFS
        # cant do dijkstras because we have k limit
        # O(E*k)
        # need temp prices array to not accidentally use additional nodes

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + price < tmpPrices[destination]:
                    tmpPrices[destination] = prices[source] + price

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]