class TrieNode:
    def __init__(self, isWord = False):
        self.isWord = isWord 
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = TrieNode()
                current = current.children[letter]
        current.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        ROWS, COLS = len(board), len(board[0])
        output = set()

        def dfs(row, col, trieNode, word = ''):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return
            if board[row][col] == '-':
                return
            if board[row][col] not in trieNode.children:
                return
            letter, board[row][col] = board[row][col], '-'
            trieNode = trieNode.children[letter]
            word += letter
            if trieNode.isWord:
                output.add(word)
            dfs(row + 1, col, trieNode, word)
            dfs(row - 1, col, trieNode, word)
            dfs(row, col + 1, trieNode, word)
            dfs(row, col - 1, trieNode, word)
            board[row][col] = letter


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie.root)
        
        return list(output)