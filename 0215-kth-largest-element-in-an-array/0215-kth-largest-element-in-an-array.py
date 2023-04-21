class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [n for n in nums if n < pivot]
        middle = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]

        L, M, R, N = len(left), len(middle), len(right), len(nums)

        if 0 <= N - k < L:
            return self.findKthLargest(left, k - M - R)
        elif 0 <= N - k - L < M:
            return pivot
        else:
            return self.findKthLargest(right, k)