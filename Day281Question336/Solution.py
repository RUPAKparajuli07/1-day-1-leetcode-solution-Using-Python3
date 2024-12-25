from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Step 1: Create a hash map of reversed words
        reverse_map = {word[::-1]: i for i, word in enumerate(words)}
        result = set()  # Use a set to avoid duplicates

        # Step 2: Iterate through each word and its index
        for i, word in enumerate(words):
            word_length = len(word)
            
            # Case 1: Handle empty string
            if word == "":
                for j, other_word in enumerate(words):
                    if i != j and other_word == other_word[::-1]:
                        result.add((i, j))
                        result.add((j, i))
                continue
            
            # Step 3: Split the word into all possible prefixes and suffixes
            for j in range(word_length + 1):
                prefix, suffix = word[:j], word[j:]
                
                # Case 2: If prefix is a palindrome and reverse of suffix exists
                if prefix == prefix[::-1] and suffix in reverse_map and reverse_map[suffix] != i:
                    result.add((reverse_map[suffix], i))
                
                # Case 3: If suffix is a palindrome and reverse of prefix exists
                # Avoid duplicates when j == 0
                if j != 0 and suffix == suffix[::-1] and prefix in reverse_map and reverse_map[prefix] != i:
                    result.add((i, reverse_map[prefix]))
        
        # Convert set to list for final output
        return list(result)
