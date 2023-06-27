class Solution:
    def maxProduct(self, s: str) -> int:
        palindromes = {}

        for bitmask in range(1, 2 ** len(s)):
            current = [s[i] for i in range(len(s)) if (bitmask & (1 << i)) > 0]
            if current == current[::-1]:
                palindromes[bitmask] = len(current)
        
        best = 0
        for bitmask1 in palindromes:
            for bitmask2 in palindromes:
                if bitmask1 & bitmask2 == 0:
                    best = max(palindromes[bitmask1] * palindromes[bitmask2], best)
        
        return best