class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, removing extra spaces
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with a single space and return the result
        return ' '.join(reversed_words)
