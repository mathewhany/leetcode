class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()

        for i, n in enumerate(nums):
            if i >= k + 1:
                visited.remove(nums[i - k - 1])
            
            if n in visited: return True

            visited.add(n)
        
        return False