class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()

        for i in range(len(s) - 10 + 1):
            key = s[i:i + 10]
            if key in seen:
                ans.add(key)
            else:
                seen.add(key)

        return list(ans)