class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        dp = [0 for _ in range(len(arr))]

        for i in range(len(arr)):
            if i == 0:
                dp[i] = (1, 1)
            else:
                prevInc, prevDec = dp[i - 1]
                dp[i] = (
                    1 + prevDec if arr[i] > arr[i - 1] else 1,
                    1 + prevInc if arr[i] < arr[i - 1] else 1,
                )

                best = max(best, max(dp[i]))
        
        return best



