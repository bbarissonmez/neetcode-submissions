class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = PrefixTreeNode()   

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTreeNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        return self.__search(word, self.root)
        
    def __search(self, word: str, node: PrefixTreeNode) -> bool:
        for index, char in enumerate(word):
            if char == '.':
                for child_node in node.children.values():
                    if self.__search(word[index+1:], child_node):
                        return True
                
                return False

            elif char not in node.children:
                return False

            node = node.children[char]

        return node.is_end
