class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        memo = {}

        def dp(start, end):
            if (start, end) in memo: return memo[(start, end)]

            ans = inf
            for cut in cuts[bisect_right(cuts, start):]:
                if cut >= end: break
                
                ans = min(ans, (end - start) + dp(start, cut) + dp(cut, end))
            
            if ans == inf: ans = 0

            memo[(start, end)] = ans
            
            return ans
        
        return dp(0, n)