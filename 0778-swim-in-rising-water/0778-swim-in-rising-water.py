class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()

        while heap:
            height, i, j = heapq.heappop(heap)

            if (i, j) in visited:
                continue

            visited.add((i, j))
            
            if i == n - 1 and j == n - 1:
                return height

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < n and (ii, jj) not in visited:
                    heapq.heappush(heap, (max(grid[ii][jj], height), ii, jj))
        
        return -1