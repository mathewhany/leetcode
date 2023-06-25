class Solution:
    def minSwaps(self, s: str) -> int:
        left, right = 0, len(s) - 1
        swaps = 0


        # ]][[[]
        countLeft, countRight = 0, 0
        while left < right:
            swapLeft, swapRight = False, False
            if s[left] == '[':
                countLeft += 1
                left += 1
            elif s[left] == ']':
                if countLeft > 0:
                    countLeft -= 1
                    left += 1
                else:
                    swapLeft = True
            if s[right] == ']':
                countRight += 1
                right -= 1
            elif s[right] == '[':
                if countRight > 0:
                    countRight -= 1
                    right -= 1
                else:
                    swapRight = True
            if swapLeft and swapRight:
                swaps += 1
                countLeft += 1
                countRight += 1
                left += 1
                right -= 1
        return swaps
            
