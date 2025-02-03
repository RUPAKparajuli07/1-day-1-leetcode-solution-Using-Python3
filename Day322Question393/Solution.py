from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Number of bytes remaining to be checked
        remaining_bytes = 0

        for num in data:
            # Get the 8 least significant bits
            byte = num & 0xFF  

            if remaining_bytes == 0:
                # Determine how many bytes the character has
                if (byte >> 7) == 0:  # 1-byte character (0xxxxxxx)
                    continue
                elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                    remaining_bytes = 3
                else:
                    return False  # Invalid starting byte
            else:
                # Check continuation byte (should be 10xxxxxx)
                if (byte >> 6) != 0b10:
                    return False
                remaining_bytes -= 1

        return remaining_bytes == 0  # All characters must be fully processed

# Example test cases
solution = Solution()
print(solution.validUtf8([197, 130, 1]))  # Output: True
print(solution.validUtf8([235, 140, 4]))  # Output: False
