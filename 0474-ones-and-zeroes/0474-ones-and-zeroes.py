class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(len(strs) - 1, -1, -1):
            for count0 in range(m + 1):
                for count1 in range(n + 1):
                    newCount0 = count0 + strs[i].count('0')
                    newCount1 = count1 + strs[i].count('1')

                    if newCount0 <= m and newCount1 <= n:
                        dp[count0][count1] = max(
                            dp[count0][count1],
                            1 + dp[newCount0][newCount1]
                        )
                    else:
                        dp[count0][count1] = dp[count0][count1]

        return dp[0][0]