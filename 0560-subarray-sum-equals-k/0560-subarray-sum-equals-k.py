class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        prefixMap = collections.defaultdict(int)
        prefixMap[0] = 1
        ans = 0
        for n in nums: 
            current = prefixSum[-1] + n
            target = current - k
            if target in prefixMap:
                ans += prefixMap[target]
            prefixSum.append(current)
            prefixMap[prefixSum[-1]] += 1
        return ans
        

