class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(start, end):
            if (start, end) in memo: return memo[(start, end)]

            if start > end: 
                return (0, 0)

            enemyScore1, myScore1 = dp(start + 1, end)
            enemyScore2, myScore2 = dp(start, end - 1)
            myScore1 += piles[start]
            myScore2 += piles[end]

            memo[(start, end)] = ans = (myScore1, enemyScore1) if myScore1 > myScore2 else (myScore2, enemyScore2)

            return ans
        
        return dp(0, len(piles) - 1)