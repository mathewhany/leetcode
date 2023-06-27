class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStrs = list(map(str, nums))
        numStrs.sort(key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1))


        if numStrs[-1] == '0':
            return '0'
            
        return ''.join(numStrs[::-1])