class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        orderedTasks = sorted([(enq, proc, i) for i, (enq, proc) in enumerate(tasks)])

        heap = []
        j = 0
        time = orderedTasks[j][0]

        ans = []

        while j < len(orderedTasks) or heap:
            while j < len(orderedTasks) and orderedTasks[j][0] <= time:
                heappush(heap, (orderedTasks[j][1], orderedTasks[j][2]))
                j += 1

            if heap:
                proc, i = heappop(heap)
                ans.append(i)
                time += proc
            elif j < len(orderedTasks):
                time = orderedTasks[j][0]

        return ans

