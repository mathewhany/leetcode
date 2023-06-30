class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left, right = nums1[:], nums2
        l, r = 0, 0

        for i in range(len(nums1)):
            if l >= m:
                nums1[i] = right[r]
                r += 1
            elif r >= n:
                nums1[i] = left[l]
                l += 1
            elif left[l] <= right[r]:
                nums1[i] = left[l]
                l += 1
            else:
                nums1[i] = right[r]
                r += 1 
