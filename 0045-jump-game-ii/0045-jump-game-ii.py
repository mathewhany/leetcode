class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([(0, nums[0], 0)])

        while queue:
            current, jumpLen, jumps = queue.popleft()

            if current == len(nums) - 1:
                return jumps
            
            for j in range(current + 1, min(len(nums), current + jumpLen + 1)):
                if nums[j] >= 0:
                    queue.append((j, nums[j], jumps + 1))
                    nums[j] = -1
        
        return -1
