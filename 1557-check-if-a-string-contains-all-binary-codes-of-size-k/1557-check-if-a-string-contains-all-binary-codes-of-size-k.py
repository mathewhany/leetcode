class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique = set()
        for i in range(len(s) - k + 1):
            key = s[i:i + k]
            unique.add(key)
        
        return len(unique) == 2 ** k