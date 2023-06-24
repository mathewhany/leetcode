class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while i < len(prices):
            j = i
            while j + 1 < len(prices) and prices[j + 1] > prices[j]: j += 1
            profit += prices[j] - prices[i]
            i = j + 1
        
        return profit
                