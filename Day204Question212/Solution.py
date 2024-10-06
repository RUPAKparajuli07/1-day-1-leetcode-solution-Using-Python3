from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word

        # Step 2: Backtracking helper function
        def backtrack(row, col, parent):
            letter = board[row][col]
            curr_node = parent.children[letter]
            
            # Check if we found a word
            if curr_node.word is not None:
                result.add(curr_node.word)
                curr_node.word = None  # Avoid duplicate entries
            
            # Mark the current cell as visited by temporarily altering the board
            board[row][col] = '#'
            
            # Explore neighbors (up, down, left, right)
            for (row_offset, col_offset) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + row_offset, col + col_offset
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if board[new_row][new_col] in curr_node.children:
                        backtrack(new_row, new_col, curr_node)
            
            # Restore the original value
            board[row][col] = letter
            
            # Optimization: prune the Trie
            if not curr_node.children:
                parent.children.pop(letter)

        # Step 3: Initialize variables and start backtracking
        result = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    backtrack(row, col, root)
        
        return list(result)
