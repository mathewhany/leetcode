class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      best = 0
      minBuy = inf

      for price in prices:
          minBuy = min(minBuy, price)
          best = max(best, price - minBuy)

      return best