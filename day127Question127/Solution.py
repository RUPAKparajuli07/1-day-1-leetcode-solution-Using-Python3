from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in the wordList, we cannot transform beginWord to endWord
        if endWord not in wordList:
            return 0
        
        # Initialize the set of words for quick lookup
        wordSet = set(wordList)
        
        # Initialize the queue for BFS
        queue = deque([(beginWord, 1)])  # (current_word, current_level)AC
        
        while queue:
            current_word, level = queue.popleft()
            
            # Try changing each character of the current word
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    # Check if the next word is the end word
                    if next_word == endWord:
                        return level + 1
                    
                    # If the next word is in the wordSet, add it to the queue for further exploration
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, level + 1))
        
        # If we exhaust the queue without finding the end word, return 0
        return 0
