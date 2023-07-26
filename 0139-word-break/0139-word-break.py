class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dp(target):
            if target in wordSet: return True
            if target in memo: return memo[target]

            for i in range(1, len(target)):
                prefix, suffix = target[:i], target[i:]
                if prefix in wordSet and dp(suffix): 
                    memo[target] = True
                    return True
            memo[target] = False
            return False

        return dp(s)