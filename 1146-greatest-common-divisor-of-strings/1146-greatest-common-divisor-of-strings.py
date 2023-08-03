class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = gcd(len(str1), len(str2))

        gcdStr = str1[:x]

        for i in range(0, len(str1), x):
            if str1[i:i+x] != gcdStr: return ""

        for i in range(0, len(str2), x):
            if str2[i:i+x] != gcdStr: return ""

        return gcdStr
        