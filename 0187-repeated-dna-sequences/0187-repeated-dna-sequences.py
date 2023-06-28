class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = defaultdict(int)
        window = []
        ans = []

        for c in s:
            window.append(c)

            if len(window) > 10:
                window.pop(0)
            
            key = ''.join(window)
            counts[key] += 1
            if counts[key] == 2: ans.append(key)
        
        return ans