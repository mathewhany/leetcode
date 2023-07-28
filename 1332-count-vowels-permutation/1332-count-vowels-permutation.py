class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        memo = {}

        def dp(lastLetter, count):
            if (lastLetter, count) in memo: return memo[(lastLetter, count)]

            if count == n:
                return 1
            
            if lastLetter == 'a':
                ans = dp('e', count + 1)
            elif lastLetter == 'e':
                ans = dp('a', count + 1) + dp('i', count + 1)
            elif lastLetter == 'i':
                ans = dp('a', count + 1) + dp('e', count + 1) + dp('o', count + 1) + dp('u', count + 1)
            elif lastLetter == 'o':
                ans = dp('i', count + 1) + dp('u', count + 1)
            elif lastLetter == 'u':
                ans = dp('a', count + 1)
            else:
                ans = dp('a', count + 1) + dp('e', count + 1) + dp('i', count + 1) + dp('o', count + 1) + dp('u', count + 1)

            memo[(lastLetter, count)] = ans

            return ans % mod

        return dp('', 0)