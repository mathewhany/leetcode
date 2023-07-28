class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[(0, 0) for _ in range(len(piles))] for _ in range(len(piles))]

        for start in range(len(piles) - 1, -1, -1):
            for end in range(start, len(piles)):
                enemyScore1, myScore1 = dp[start + 1][end] if start + 1 < len(piles) else (0, 0)
                enemyScore2, myScore2 = dp[start][end - 1] if end - 1 >= start else (0, 0)
                myScore1 += piles[start]
                myScore2 += piles[end]

                dp[start][end] = (myScore1, enemyScore1) if myScore1 > myScore2 else (myScore2, enemyScore2)


        return dp[0][len(piles) - 1]