class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words
        
        # If lengths mismatch, it cannot follow the pattern
        if len(pattern) != len(words):
            return False
        
        # Dictionaries for bijection
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check if character-to-word mapping is consistent
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # Check if word-to-character mapping is consistent
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
