class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A
        
        halfSize = (len(A) + len(B)) // 2
        l, r = 0, len(A) - 1

        while True:
            mid = (l + r) // 2

            AleftIdx, BleftIdx = mid, halfSize - mid - 2
            ArightIdx, BrightIdx = AleftIdx + 1, BleftIdx + 1

            Aleft = A[AleftIdx] if AleftIdx >= 0 else -inf
            Bleft = B[BleftIdx] if BleftIdx >= 0 else -inf
            Aright = A[ArightIdx] if ArightIdx < len(A) else inf
            Bright = B[BrightIdx] if BrightIdx < len(B) else inf

            if Aleft > Bright:
                r = mid - 1
            elif Aright < Bleft:
                l = mid + 1
            else:
                leftHalfLast = max(Aleft, Bleft)
                rightHalfFirst = min(Aright, Bright)

                if (len(A) + len(B)) % 2 == 0:
                    return (leftHalfLast + rightHalfFirst) / 2
                
                return rightHalfFirst
                    