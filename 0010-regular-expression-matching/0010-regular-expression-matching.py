class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= S and j >= P:
                return True

            if j >= P:
                return False

            print(i < S and s[i], p[j])
            answer = memo[(i, j)] = (
                i < S and (s[i] == p[j] or p[j] == '.') and dp(i + 1, j) or
                dp(i, j + 2)
            ) if (j + 1 < P and p[j + 1] == '*') else (
                i < S and (p[j] == '.' or s[i] == p[j]) and dp(i + 1, j + 1)
            )

            return answer
        

        return dp(0, 0)