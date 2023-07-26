class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]: continue
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet:
                    dp[j] = True
                if dp[len(s)]:
                    return True

        return False