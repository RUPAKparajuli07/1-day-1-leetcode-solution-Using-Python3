class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            columnNumber -= 1  # Decrement to make the range 0-25 instead of 1-26
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result  # 65 is the ASCII code for 'A'
            columnNumber //= 26  # Move to the next digit
        
        return result
