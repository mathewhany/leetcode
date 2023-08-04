class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        ans = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        boundaryChanges = [
            (1, 0, 0, 0),
            (0, 0, 0, -1),
            (0, -1, 0, 0),
            (0, 0, 1, 0),
        ]
        state = 0

        i, j = 0, 0
        while top <= i <= bottom and left <= j <= right:
            ans.append(matrix[i][j])

            di, dj = directions[state]
            ii, jj = i + di, j + dj

            if not (top <= ii <= bottom and left <= jj <= right):
                dTop, dBottom, dLeft, dRight = boundaryChanges[state]
                top += dTop
                bottom += dBottom
                left += dLeft
                right += dRight
                state = (state + 1) % 4
                di, dj = directions[state]
            
            i += di
            j += dj

        return ans