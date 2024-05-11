class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing whitespaces
        s = s.rstrip()
        # Split the string by spaces and get the last element
        last_word = s.split()[-1]
        # Return the length of the last word
        return len(last_word)
