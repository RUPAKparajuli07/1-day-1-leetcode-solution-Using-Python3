class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Calculate the value for the current character
            value = ord(char) - ord('A') + 1
            # Update the result by shifting left and adding the new value
            result = result * 26 + value
        return result
