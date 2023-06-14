class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(numRows - 1):
            ans.append([])
            ans[-1].append(1)
            for j in range(i):
                ans[-1].append(ans[-2][j] + ans[-2][j + 1])
            ans[-1].append(1) 

        return ans