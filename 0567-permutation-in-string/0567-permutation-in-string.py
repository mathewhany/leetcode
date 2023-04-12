from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        window = Counter(s1)
        needed = len(s1)
        requiredLetters = set(s1)

        for i, l in enumerate(s2):
            if l in requiredLetters:
                if window[l] > 0: needed -= 1
                window[l] -= 1
            
            if i + 1 > len(s1):
                windowStart = i - len(s1)
                startLetter = s2[windowStart]

                if startLetter in requiredLetters:
                    window[startLetter] += 1
                    if window[startLetter] > 0: needed += 1

            if needed == 0:
                return True
        
        return False

