class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))

        heapify(nums)

        for _ in range(len(nums) - k):
            heappop(nums)

        return str(heappop(nums))

        