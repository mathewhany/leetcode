class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        prefixSum = [0]
        for s in stones: prefixSum.append(s + prefixSum[-1])
        
        dp = [[[inf for _ in range(k + 1)] for _ in range(len(stones))] for _ in range(len(stones))]

        for i in range(len(stones) - 1, -1, -1):
            for j in range(i, len(stones)):
                for piles in range(k, 0, -1):
                    if i == j:
                        dp[i][j][piles] = 0 if piles == 1 else inf
                    elif piles == 1:
                        dp[i][j][piles] = dp[i][j][k] + prefixSum[j + 1] - prefixSum[i]
                    else:
                        dp[i][j][piles] = min(
                            dp[i][mid][1] + dp[mid + 1][j][piles - 1] for mid in range(i, j)
                        )

        ans = dp[0][len(stones) - 1][1]

        return ans if ans != inf else -1
