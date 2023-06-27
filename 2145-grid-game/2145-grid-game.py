class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix1, prefix2 = [], []
        for n1, n2 in zip(*grid):
            prefix1.append((prefix1[-1] if prefix1 else 0) + n1)
            prefix2.append((prefix2[-1] if prefix2 else 0) + n2)
        
        best = inf
        for i in range(n):
            best = min(max(prefix1[-1] - prefix1[i], prefix2[i - 1] if i > 0 else 0), best)
        
        return best