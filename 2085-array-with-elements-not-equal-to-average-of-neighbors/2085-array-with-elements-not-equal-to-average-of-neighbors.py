class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        for i in range(0, len(nums) // 2, 2):
            key = (len(nums) - 1 - i if len(nums) % 2 == 0 else len(nums) - 2 - i)
            nums[i], nums[key] = nums[key], nums[i]

        return nums