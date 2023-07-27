class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if not (0 <= i < n and 0 <= j < m): return 0

            if text1[i] == text2[j]: 
                ans = 1 + dp(i + 1, j + 1)
            else:
                ans = max(
                    dp(i + 1, j),
                    dp(i, j + 1)
                )
            memo[(i, j)] = ans
            
            return ans
        
        return dp(0, 0)