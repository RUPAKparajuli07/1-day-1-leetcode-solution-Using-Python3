class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Boolean to mark if this node represents the end of a word
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        # Root node does not store any character
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root node
        node = self.root
        for char in word:
            # If the character is not in the current node, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node
            node = node.children[char]
        # After inserting all characters, mark the end of the word
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Start from the root node
        node = self.root
        for char in word:
            # If the character is not in the node, return False
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # Check if we are at the end of a word
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        node = self.root
        for char in prefix:
            # If the character is not in the node, return False
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # If all characters in the prefix are found, return True
        return True


# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app"))     # True
