class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for _ in range(numRows - 1):
            ans.append([a + b for a, b in zip([0] + ans[-1], ans[-1] + [0])])

        return ans