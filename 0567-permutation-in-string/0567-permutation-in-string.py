from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        def key(letter):
            return ord(letter) - ord('a')

        window = [0] * 26
        needed = 0
        for l in s1:
            window[key(l)] -= 1
            needed += 1

        requiredLetters = set(s1)
        windowStart = 0

        for i, l in enumerate(s2):
            window[key(l)] += 1
            if l in requiredLetters and window[key(l)] <= 0:
                needed -= 1
            
            if i - windowStart + 1 > len(s1):
                startLetter = s2[windowStart] 
                window[key(startLetter)] -= 1
                windowStart += 1

                if startLetter in requiredLetters and window[key(startLetter)] < 0:
                    needed += 1
            
            if needed == 0:
                return True
        
        return False

