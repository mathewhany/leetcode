class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1: return 1

        lines = defaultdict(set)

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if (x1, y1) != (x2, y2):
                    if x2 - x1 == 0:
                        slope = inf
                        c = x1
                    else:
                        slope = (y2 - y1) / (x2 - x1)
                        c = y1 - slope * x1

                    lines[(slope, c)].add((x1, y1))
                    lines[(slope, c)].add((x2, y2))

        best = -inf
        for line in lines.values():
            best = max(best, len(line))

        return best