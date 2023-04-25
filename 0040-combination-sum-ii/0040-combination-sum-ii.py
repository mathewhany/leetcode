class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []
        current = []
        currentSum = 0

        def backtrack(i):
            nonlocal currentSum 

            if currentSum > target:
                return

            if i >= len(candidates):
                if currentSum == target:
                    output.append(current[:])
                return
            
            current.append(candidates[i])
            currentSum += candidates[i]
            backtrack(i + 1)
            currentSum -= current.pop()
            
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)

        return output