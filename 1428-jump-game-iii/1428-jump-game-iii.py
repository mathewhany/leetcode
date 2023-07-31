class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set([start])

        while queue:
            i = queue.popleft()
            if arr[i] == 0: return True
            
            for j in [i + arr[i], i - arr[i]]:
                if j not in visited and 0 <= j < len(arr):
                    visited.add(j)
                    queue.append(j)
        
        return False