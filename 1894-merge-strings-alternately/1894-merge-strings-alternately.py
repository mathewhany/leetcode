class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p, q = 0, 0
        ans = []
        for i in range(len(word1) + len(word2)):
            if i % 2 == 0 and p < len(word1) or q >= len(word2):
                ans.append(word1[p])
                p += 1
            else:
                ans.append(word2[q])
                q += 1

        return ''.join(ans)