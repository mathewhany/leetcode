class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first, last = {}, {}
        
        for i, letter in enumerate(s):
            if letter not in first:
                first[letter] = last[letter] = i
            else:
                last[letter] = i
        
        ans = 0
        for letter in first:
            start, end = first[letter], last[letter]
            if end - start + 1 >= 3:
                ans += len(set(s[start + 1:end]))
        return ans
            
                