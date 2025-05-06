from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define sets for each keyboard row
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            lower_word = set(word.lower())
            # Check if all letters of the word are in one of the rows
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                result.append(word)
                
        return result
