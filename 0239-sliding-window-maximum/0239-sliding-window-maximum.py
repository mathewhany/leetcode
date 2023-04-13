class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapq.heapify(h)
        output = []

        for i, n in enumerate(nums):
            heapq.heappush(h, (-n, i))

            if i + 1 >= k:
                while h[0][1] < i - k + 1:
                    heapq.heappop(h)
                output.append(-h[0][0])

        return output