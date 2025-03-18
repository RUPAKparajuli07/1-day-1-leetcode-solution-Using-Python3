from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write the compressed character
        read = 0   # Position to read characters
        
        while read < len(chars):
            char = chars[read]  # Get the current character
            count = 0  # Initialize count for this character
            
            # Count consecutive occurrences of the character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the compressed array
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):  # Convert count to string and write each digit separately
                    chars[write] = digit
                    write += 1
        
        return write  # The length of the compressed array
