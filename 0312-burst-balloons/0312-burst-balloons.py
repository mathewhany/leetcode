class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        memo = {}

        dp = [[0] * N for _ in range(N)]

        for length in range(3, N + 1):
            for start in range(0, N - length + 1):
                end = start + length - 1
                for i in range(start + 1, end):
                    dp[start][end] = max(dp[start][end], dp[start][i] + nums[start] * nums[i] * nums[end] + dp[i][end])

        
        return dp[0][N - 1]