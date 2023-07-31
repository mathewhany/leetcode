class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        memo = {}

        def dp(i):
            if i in memo: return memo[i]

            if i == len(arr) - 1:
                return (1, 1)

            nextIncreasing, nextDecreasing = dp(i + 1)
            
            memo[i] = ans = (
                1 + nextDecreasing if arr[i] < arr[i + 1] else 1,
                1 + nextIncreasing if arr[i] > arr[i + 1] else 1,   
            )

            return ans
        
        best = 0
        for i in range(len(arr)):
            increasing, decreasing = dp(i)
            best = max(best, increasing, decreasing)
        
        return best



