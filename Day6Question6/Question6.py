class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through each character in the string
        for char in s:
            # Add the current character to the current row
            rows[current_row] += char
            
            # If we're at the top or bottom row, switch directions
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row based on the current direction
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to get the final string
        return ''.join(rows)

# Example usage
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(sol.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(sol.convert("A", 1))               # Output: "A"
