class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        output = []

        def backtrack(i):
            if i >= len(nums):
                output.append(subset[:])
                return
            
            backtrack(i + 1)
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

        backtrack(0)

        return output
            