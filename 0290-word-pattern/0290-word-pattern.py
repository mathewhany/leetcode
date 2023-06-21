class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False
            
        dictA, dictB = {}, {}

        for a, b in zip(pattern, s.split(" ")):
            if a not in dictA and b not in dictB:
                dictA[a] = b
                dictB[b] = a
            elif (a in dictA) ^ (b in dictB) or b != dictA[a] or a != dictB[b]:
                return False
        
        return True

