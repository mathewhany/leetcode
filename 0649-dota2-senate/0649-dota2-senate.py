class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue = deque()
        dQueue = deque()
        n = len(senate)

        for i, x in enumerate(senate):
            if x == 'R': rQueue.append(i)
            else: dQueue.append(i)
        

        while rQueue and dQueue:
            if rQueue[0] < dQueue[0]:
                dQueue.popleft()
                rQueue.popleft()
                rQueue.append(n + 1)
            else:
                rQueue.popleft()
                dQueue.popleft()
                dQueue.append(n + 1)
            n += 1
        
        if rQueue:
            return 'Radiant'
        
        return 'Dire'