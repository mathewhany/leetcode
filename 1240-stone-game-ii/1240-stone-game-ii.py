class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def dp(i, m):
            if (i, m) in memo: return memo[(i, m)]

            if i >= len(piles): return (0, 0)

            currentSum = 0
            bestScore = 0
            worstEnemyScore = inf

            for x in range(1, 2 * m + 1):
                if i + x - 1 >= len(piles): break 
                currentSum += piles[i + x - 1]
                enemyScore, myRestScore = dp(i + x, max(x, m))
                myScore = currentSum + myRestScore
                if myScore > bestScore:
                    bestScore = myScore
                    worstEnemyScore = enemyScore
            
            memo[(i, m)] = ans = (bestScore, worstEnemyScore)

            return ans

        myScore, _ = dp(0, 1)

        return myScore