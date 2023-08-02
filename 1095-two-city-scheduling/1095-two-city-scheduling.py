class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum(aCost for aCost, _ in costs) + sum(sorted([bCost - aCost for aCost, bCost in costs])[:len(costs) // 2])