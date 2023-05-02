class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [0 if i == src else inf for i in range(n)]

        for _ in range(k + 1):
            newPrices = prices[:]
            for f, t, d in flights:
                newPrices[t] = min(newPrices[t], prices[f] + d)
            prices = newPrices
        
        return prices[dst] if prices[dst] != inf else -1