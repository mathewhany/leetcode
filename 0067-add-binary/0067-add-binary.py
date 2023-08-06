class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        q = deque()

        while i >= 0 or j >= 0:
            valA = int(a[i]) if i >= 0 else 0
            valB = int(b[j]) if j >= 0 else 0

            ans = (valA + valB + carry) % 2
            carry = (valA + valB + carry) // 2

            q.appendleft(str(ans))
            i -= 1
            j -= 1
        
        if carry:
            q.appendleft(str(carry))
        
        return ''.join(q)