class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [0]
        for n in nums: prefixSum.append(n + prefixSum[-1])

        best = inf

        for l in range(len(nums)):
            lo, hi = l + 1, len(nums)
            ans = -1

            while lo <= hi:
                mid = (lo + hi) // 2
                if prefixSum[mid] - prefixSum[l] >= target:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            if ans > -1: best = min(best, ans - l)
        
        return best if best != inf else 0
