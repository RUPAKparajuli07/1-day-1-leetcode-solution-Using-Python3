class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces to get each word
        words = s.split()
        
        # Reverse each word and collect in a list
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words using space and return the result
        return ' '.join(reversed_words)
