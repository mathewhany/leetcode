class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        reversedX = 0
        tmpX = x

        while tmpX > 0:
            reversedX = reversedX * 10 + tmpX % 10
            tmpX //= 10
        
        return reversedX == x