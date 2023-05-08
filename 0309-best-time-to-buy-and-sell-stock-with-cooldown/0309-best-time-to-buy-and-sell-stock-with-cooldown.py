class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cooldown = 0, -inf, -inf
        best = 0

        for price in prices:
            (
                buy, 
                sell, 
                cooldown
            ) = (
                max(buy, cooldown),
                max(sell, buy - price),
                sell + price
            )
        
        return max(buy, cooldown)