def intersects(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    return not (start2 > end1 or start1 > end2)

def merge(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    return (min(start1, start2), max(end1, end2))

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        intervals = deque([(0, 0)])

        while intervals:
            start, end = intervals.popleft()

            i = start
            while i <= min(end, len(s) - 1):
                if s[i] == '0':
                    if i == len(s) - 1: return True

                    nextStart, nextEnd = nextInterval = (i + minJump, i + maxJump)

                    if nextStart <= end:
                        end = nextEnd 
                    else:
                        if not intervals or not intersects(intervals[-1], nextInterval):
                            intervals.append(nextInterval)
                        else:
                            intervals.append(merge(intervals.pop(), nextInterval))
                i += 1

        return False