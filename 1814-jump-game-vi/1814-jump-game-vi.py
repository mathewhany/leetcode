
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        maxWindow = deque()
        dp = [0 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = nums[i]
                maxWindow.append((nums[i], i))
            
            else:
                restMax = maxWindow[-1][0]
                
                dp[i] = nums[i] + restMax

                windowStart = i
                windowEnd = i + k - 1

                while maxWindow and maxWindow[-1][1] > windowEnd:
                    maxWindow.pop()
                
                while maxWindow and maxWindow[0][0] < dp[i]:
                    maxWindow.popleft()
                
                maxWindow.appendleft((dp[i], i))
        
        return dp[0]


