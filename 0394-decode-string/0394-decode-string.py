class Solution:
    def decodeString(self, s: str) -> str:
        words = ['']
        counts = []
        currentCount = []

        for c in s:
            if c in string.ascii_lowercase:
                words.append(c)
            elif c == '[':
                counts.append(int(''.join(currentCount)))
                currentCount = []
                words.append('[')
            elif c == ']':
                word = []
                while words and words[-1] != '[':
                    word.append(words.pop())
                words.pop()
                words.append(''.join(word[::-1]) * counts.pop())
            else:
                currentCount.append(c)

        return ''.join(words)
