class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        preMap = defaultdict(set)
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pre, next in prerequisites:
            adj[pre].append(next)
            indegrees[next] += 1

        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            course = q.popleft()
            for next in adj[course]:
                indegrees[next] -= 1
                preMap[next].add(course)
                preMap[next].update(preMap[course])
                if indegrees[next] == 0:
                    q.append(next)
                    
        return [a in preMap[b] for a, b in queries]

                