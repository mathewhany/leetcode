class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, k - 1

        for i in range(k, len(arr)):
            if abs(arr[i] - x) < abs(arr[start] - x) or arr[i] == arr[start]:
                start += 1
                end += 1
            else:
                break
        
        return arr[start:end + 1]

