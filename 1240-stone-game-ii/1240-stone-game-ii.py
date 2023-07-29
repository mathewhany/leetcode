class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[(0, 0) for _ in range(n + 1)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                currentSum = 0
                bestScore = 0
                worstEnemyScore = inf

                for x in range(1, 2 * m + 1):
                    if i + x - 1 >= len(piles): break 
                    currentSum += piles[i + x - 1]
                    enemyScore, myRestScore = dp[i + x][max(x, m)]
                    myScore = currentSum + myRestScore
                    if myScore > bestScore:
                        bestScore = myScore
                        worstEnemyScore = enemyScore
                
                dp[i][m] = (bestScore, worstEnemyScore)

        myScore, _ = dp[0][1]

        return myScore