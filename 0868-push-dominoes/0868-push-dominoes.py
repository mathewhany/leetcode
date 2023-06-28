class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = []
        count = 0

        for i, d in enumerate(dominoes):
            if d != '.':
                if ans and ans[-1] == 'R' and d == 'L':
                    for _ in range(count // 2): ans.append('R')
                    if count % 2 == 1: ans.append('.')
                    for _ in range(count // 2): ans.append('L')
                elif ans and ans[-1] == 'R':
                    for _ in range(count): ans.append('R')
                elif d == 'L':
                    for _ in range(count): ans.append('L')
                else:
                    for _ in range(count): ans.append('.')
                count = 0
                ans.append(d)
            else:
                count += 1
        
        if count > 0:
            if ans and ans[-1] == 'R':
                for _ in range(count): ans.append('R')
            else:
                for _ in range(count): ans.append('.')
        
        return ''.join(ans)

