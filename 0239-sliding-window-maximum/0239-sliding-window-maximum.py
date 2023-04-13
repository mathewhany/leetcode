class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        output = []

        for i, n in enumerate(nums):
            while dq and n > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

            windowStart = i - k + 1
            if dq[0] < windowStart:
                dq.popleft()

            if i + 1 >= k:
                output.append(nums[dq[0]])
                windowStart += 1

        return output