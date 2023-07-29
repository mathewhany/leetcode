class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        memo = {}        
        def dp(i, lastChar):
            if (i, lastChar) in memo: return memo[(i, lastChar)]

            if i >= len(s): 
                return 0

            if lastChar == 1:
                ans = (s[i] == '0') + dp(i + 1, 1)
            else:
                ans = min((s[i] == '1') + dp(i + 1, 0), (s[i] == '0') + dp(i + 1, 1))
            
            memo[(i, lastChar)] = ans
            
            return ans
        
        return dp(0, 0)