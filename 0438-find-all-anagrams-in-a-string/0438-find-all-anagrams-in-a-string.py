class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pMap = Counter(p)
        sMap = collections.defaultdict(int)
        ans = []

        for i, l in enumerate(s):   
            sMap[l] += 1
         
            if i >= len(p) - 1:
                isAnagram = True
                for c in pMap:
                    if sMap[c] != pMap[c]:
                        isAnagram = False
                        break
                if isAnagram:
                    ans.append(i - len(p) + 1)

                sMap[s[i - len(p) + 1]] -= 1
        
        return ans