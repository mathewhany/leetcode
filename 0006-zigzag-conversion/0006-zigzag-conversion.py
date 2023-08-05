class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]

        for i, c in enumerate(s):
            row = i % (2 * numRows - 2) if numRows > 2 else i % numRows

            if row < numRows:
                rows[row].append(c)
            else:
                rows[numRows - 2 - (row - numRows)].append(c)
        
        return ''.join(''.join(row) for row in rows)