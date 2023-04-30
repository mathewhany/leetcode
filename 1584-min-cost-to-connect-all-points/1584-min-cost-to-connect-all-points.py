def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pointsSet = set(map(tuple, points))
        heap = [(0, tuple(points[0]))]
        totalCost = 0

        while pointsSet:
            cost, point = heapq.heappop(heap)
            if point not in pointsSet:
                continue
            
            pointsSet.remove(point)
            totalCost += cost

            for otherPoint in pointsSet:
                dist = distance(point, otherPoint)
                heapq.heappush(heap, (dist, otherPoint))
        
        return totalCost