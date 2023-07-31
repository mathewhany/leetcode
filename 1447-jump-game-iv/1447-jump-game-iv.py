class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque([(0, 0)])
        visited = set([0])

        equals = defaultdict(list)
        for i, n in enumerate(arr):
            equals[n].append(i)

        while queue:
            i, jumps = queue.popleft()

            if i == len(arr) - 1:
                return jumps
            
            for j in equals[arr[i]] + [i + 1, i - 1]:
                if i != j and 0 <= j < len(arr) and j not in visited:
                    visited.add(j)
                    queue.append((j, jumps + 1))
            equals[arr[i]] = []
                        
        return -1
