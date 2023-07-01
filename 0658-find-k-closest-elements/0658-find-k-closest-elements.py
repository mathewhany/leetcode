class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def cmp(a, b):
            if abs(a - x) < abs(b - x):
                return -1
            elif abs(b - x) < abs(a - x):
                return 1
            elif a < b:
                return -1
            elif b > a:
                return 1
            else:
                return 0

        arr.sort(key=cmp_to_key(cmp))

        return sorted(arr[:k])