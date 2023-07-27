class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            y, x = -heappop(stones), -heappop(stones)
            if y != x: 
                heappush(stones, -(y - x))

        return -heappop(stones) if stones else 0