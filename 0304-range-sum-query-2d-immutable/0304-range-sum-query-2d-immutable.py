class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.prefix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                top = self.prefix[i - 1][j] if i > 0 else 0
                left = self.prefix[i][j - 1] if j > 0 else 0
                topLeft = self.prefix[i - 1][j - 1] if i > 0 and j > 0 else 0

                self.prefix[i][j] = matrix[i][j] + top + left - topLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        topLeft = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return self.prefix[row2][col2] - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)