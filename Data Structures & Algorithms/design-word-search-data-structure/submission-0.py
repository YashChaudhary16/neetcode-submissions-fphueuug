class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str, node = None) -> bool:

        if node is None:
            node = self.root

        for i in range(len(word)):
            
            ch = word[i]

            if ch == ".":
                for child in node.children:
                    child_node = node.children[child]
                    if self.search(word[i+1:], child_node):
                        return True  # Found a valid path!
                return False  # Tried all children and none matched
            else:
                if ch not in node.children:
                    return False
                
                node = node.children[ch]
            
        return node.is_end
        
