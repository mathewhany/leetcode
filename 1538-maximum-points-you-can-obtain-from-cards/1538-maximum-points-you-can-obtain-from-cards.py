class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        minWindowScore = inf
        windowScore = 0
        windowStart = 0
        reqWindowSize = len(cardPoints) - k
        summation = 0

        for windowEnd, pts in enumerate(cardPoints):
            summation += pts
            windowScore += pts
            windowSize = windowEnd - windowStart + 1

            if windowSize > reqWindowSize:
                windowScore -= cardPoints[windowStart]
                windowStart += 1
                windowSize -= 1
            
            if windowSize == reqWindowSize:
                minWindowScore = min(minWindowScore, windowScore)
        
        return summation - minWindowScore