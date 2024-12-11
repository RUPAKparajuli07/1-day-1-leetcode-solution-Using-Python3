from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Step 1: Precompute bitmasks and lengths
        n = len(words)
        bitmasks = []
        lengths = []
        
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))  # Set the bit for the character
            bitmasks.append(bitmask)
            lengths.append(len(word))
        
        # Step 2: Compute maximum product
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:  # No common letters
                    max_product = max(max_product, lengths[i] * lengths[j])
        
        return max_product
