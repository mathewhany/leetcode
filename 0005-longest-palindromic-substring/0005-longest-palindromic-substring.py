class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestStart, bestEnd = 0, 0

        def helper(i, j):
            nonlocal bestStart, bestEnd
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > bestEnd - bestStart:
                    bestStart, bestEnd = i, j + 1
                j += 1
                i -= 1


        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        
        return s[bestStart:bestEnd]
            
