class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for f, t in tickets:
            heapq.heappush(graph[f], t)
            
        output = []
        def dfs(f):
            while graph[f]:
                t = heapq.heappop(graph[f])
                dfs(t)
            output.append(f)

        dfs("JFK")

        return reversed(output)