class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        dp = [0 for _ in range(len(arr))]

        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                dp[i] = (1, 1)
            else:
                nextInc, nextDec = dp[i + 1]
                dp[i] = (
                    1 + nextDec if arr[i] < arr[i + 1] else 1,
                    1 + nextInc if arr[i] > arr[i + 1] else 1,
                )

                best = max(best, max(dp[i]))
        
        return best



