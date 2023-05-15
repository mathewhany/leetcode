class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        currentTank = 0
        best = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            currentTank += g - c
            
            if currentTank < 0:
                currentTank = 0
                best = i + 1
        
        if tank >= 0:
            return best
        
        return -1
