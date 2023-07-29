class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wordLen = len(words[0])
        letterMap = [[0 for _ in range(26)] for _ in range(wordLen)]
        mod = 10 ** 9 + 7
        
        for word in words:
            for i, letter in enumerate(word):
                letterMap[i][ord(letter) - ord('a')] += 1
        
        memo = {}
        def dp(i, k):
            if (i, k) in memo: 
                return memo[(i, k)]

            if i >= len(target): 
                return 1

            if k >= wordLen: 
                return 0
            
            ans = letterMap[k][ord(target[i]) - ord('a')] * dp(i + 1, k + 1) + dp(i, k + 1)
            
            memo[(i, k)] = ans

            return ans % mod
        
        return dp(0, 0)