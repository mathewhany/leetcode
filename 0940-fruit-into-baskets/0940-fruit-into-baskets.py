class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best = 0
        l = 0
        basket = defaultdict(int)

        for r, t in enumerate(fruits):
            basket[t] += 1
            
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            
            best = max(best, r - l + 1)
        
        return best
