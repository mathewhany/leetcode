class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for buy, sell in zip(prices, prices[1:]):
            profit += max(sell - buy, 0)
        
        return profit
                