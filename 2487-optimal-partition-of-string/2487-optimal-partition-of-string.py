class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        for c in s:
            if c in seen:
                count += 1
                seen.clear()
            seen.add(c)

        return count