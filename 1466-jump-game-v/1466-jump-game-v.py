class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}

        def dp(i):
            if i in memo: return memo[i]

            maxLeft, maxRight = 0, 0

            for j in range(i + 1, min(i + d + 1, len(arr))):
                if arr[i] > arr[j]:
                    maxRight = max(maxRight, dp(j))
                else:
                    break

            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[i] > arr[j]:
                    maxLeft = max(maxLeft, dp(j))
                else:
                    break
            
            memo[i] = ans = 1 + max(maxRight, maxLeft)

            return ans
        
        return max(dp(i) for i in range(len(arr)))
             