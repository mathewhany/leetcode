class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([beginWord])
        pathLength = 0

        while queue:
            pathLength += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return pathLength
                for i in range(len(word)):
                    for letter in string.ascii_lowercase:
                        nextWord = word[:i] + letter + word[i + 1:]
                        if nextWord in wordSet:
                            wordSet.remove(nextWord)
                            queue.append(nextWord)
        
        return 0