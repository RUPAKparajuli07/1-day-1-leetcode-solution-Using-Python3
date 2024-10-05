class TrieNode:
    def __init__(self):
        # Store children nodes and whether this node marks the end of a word
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        # Root node of the Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        # Helper function to perform DFS search in the Trie
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            
            char = word[i]
            if char == '.':
                # If current character is '.', try all possible child nodes
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # If current character is not '.', move to the corresponding child node
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        
        # Start DFS from the root node
        return dfs(self.root, 0)

# Example usage:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))  # False
# print(obj.search("bad"))  # True
# print(obj.search(".ad"))  # True
# print(obj.search("b.."))  # True
