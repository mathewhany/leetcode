class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        prefixSum = [0]
        for s in stones: prefixSum.append(s + prefixSum[-1])
        
        memo = {}

        def dp(i, j, piles):
            if (i, j, piles) in memo: return memo[(i, j, piles)]

            if i == j: 
                return 0 if piles == 1 else inf

            if piles == 1:
                ans = dp(i, j, k) + prefixSum[j + 1] - prefixSum[i]
            else:
                ans = inf

                for mid in range(i, j):
                    ans = min(
                        ans, 
                        dp(i, mid, 1) + dp(mid + 1, j, piles - 1)
                    )

            memo[(i, j, piles)] = ans
            
            return ans

        ans = dp(0, len(stones) - 1, 1)

        return ans if ans != inf else -1
