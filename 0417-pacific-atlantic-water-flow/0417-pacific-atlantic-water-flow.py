class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(i, j, prev, visited):
            if (not (0 <= i < ROWS and 0 <= j < COLS) or 
                (i, j) in visited or
                heights[i][j] < prev):
                return

            visited.add((i, j))
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)
        
        pac, atl = set(), set()

        for i in range(ROWS):
            dfs(i, 0, -inf, pac)
            dfs(i, COLS - 1, -inf, atl)
        for i in range(COLS):
            dfs(0, i, -inf, pac)
            dfs(ROWS - 1, i, -inf, atl)
        
        return list(pac & atl)
