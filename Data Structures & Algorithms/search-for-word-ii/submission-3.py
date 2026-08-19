class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for index, word in enumerate(words):
            trie.insert(index, word)

        result = []

        def dfs(row, col, node):
            nonlocal result

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return

            char = board[row][col]

            if char in node.children:
                parent = node
                node = node.children[char]

                if node.index != -1:
                    result.append(words[node.index])
                    node.index = -1
                    
                temp = board[row][col]

                board[row][col] = '#'
                
                dfs(row+1, col, node)
                dfs(row, col+1, node)
                dfs(row-1, col, node)
                dfs(row, col-1, node)

                board[row][col] = temp

                if not node.children and node.index == -1:
                    del parent.children[char]

            else:

                return
            

        for row in range (len(board)):
            for col in range (len(board[0])):
                dfs(row, col, trie.root)

        return result


class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()           

    def insert(self, index: int, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTreeNode()

            node = node.children[char]

        node.index = index
        

        
        