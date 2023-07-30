class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        memo = {}
        def dp(start, length):
            if (start, length) in memo: return memo[(start, length)]
            ans = inf

            for cut in cuts[bisect_right(cuts, start):]:
                if cut >= start + length: break

                leftLen = cut - start
                rightLen = length - leftLen

                ans = min(ans, length + dp(start, leftLen) + dp(cut, rightLen))
            memo[(start, length)] = ans if ans != inf else 0
            return ans if ans != inf else 0
        
        return dp(0, n)