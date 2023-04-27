class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if not (0 <= i < ROWS and 0 <= j < COLS) or board[i][j] != 'O':
                return
            
            board[i][j] = '-'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
                    
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                board[row][col] = 'O' if board[row][col] == '-' else 'X'
