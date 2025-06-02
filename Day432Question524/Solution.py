from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word):
            # Check if word is a subsequence of s
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            return i == len(word)
        
        # Sort dictionary: longer words first, then lexicographically smaller ones
        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if is_subsequence(word):
                return word

        return ""
