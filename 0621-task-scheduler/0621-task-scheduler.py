class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(heap)

        queue = deque()
        time = 0

        while queue or heap:
            if heap:
                negCount, task = heapq.heappop(heap)
                if negCount + 1 < 0:
                    queue.append((time + n + 1, negCount + 1, task))
            time += 1
            while queue and queue[0][0] <= time:
                blockedTask = queue.popleft()
                heapq.heappush(heap, (blockedTask[1], blockedTask[2]))

        return time
