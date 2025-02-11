class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1  # Number of digits in the current range
        count = 9   # Total numbers in this range
        start = 1   # First number in the current range

        # Step 1: Identify the range in which 'n' falls
        while n > length * count:
            n -= length * count  # Reduce n by the number of digits in this range
            length += 1          # Move to the next range (1-digit -> 2-digit -> 3-digit...)
            count *= 10          # Increase count (9, 90, 900, ...)
            start *= 10          # Move start to the next range (1, 10, 100, ...)

        # Step 2: Find the exact number
        number = start + (n - 1) // length  # Identify the number containing the nth digit

        # Step 3: Find the exact digit
        digit_index = (n - 1) % length  # Find the index of the digit in the number
        return int(str(number)[digit_index])  # Convert number to string and extract the digit

# Example Test Cases
sol = Solution()
print(sol.findNthDigit(3))   # Output: 3
print(sol.findNthDigit(11))  # Output: 0
