class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1  # Only 0 is valid
        
        total = 1  # For n = 0, the result is 1
        for i in range(1, n + 1):
            count = 9  # First digit (1-9)
            available_digits = 9  # Remaining digits (0-9 excluding used digits)
            for j in range(1, i):  # Fill the remaining i-1 digits
                count *= available_digits
                available_digits -= 1
            total += count
        return total
