class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        
        for spell in spells:
            lo, hi = 0, len(potions) - 1
            ans = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                if spell * potions[mid] >= success:
                    ans = len(potions) - mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            pairs.append(ans)

        return pairs