class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        memo = {}
        def dp(i, prev):
            if (i, prev) in memo:
                return memo[(i, prev)]

            if i >= len(flowerbed):
                return 0
            
            next = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
            current = flowerbed[i]

            ans = memo[(i, prev)] = max(1 + dp(i + 2, next), dp(i + 1, 0)) if prev + next + current == 0 else dp(i + 1, current)

            return ans
        return dp(0, 0) >= n