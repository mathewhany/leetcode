class Solution:
    def numTrees(self, N: int) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]

            if n < 2: return 1

            ans = 0
            for i in range(1, n + 1):
                left, right = i - 1, n - i

                ans += dfs(left) * dfs(right)
            
            memo[n] = ans
            
            return ans

        return dfs(N)