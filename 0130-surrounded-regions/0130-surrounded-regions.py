class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if not (0 <= i < ROWS and 0 <= j < COLS) or board[i][j] != 'O':
                return
            
            board[i][j] = '-'
            for di, dj in DIRS:
                dfs(i + di, j + dj)
                    
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for col in range(1, COLS - 1):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                board[row][col] = 'O' if board[row][col] == '-' else 'X'
