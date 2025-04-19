class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9  # Only single digit palindrome
        
        high = 10 ** n - 1
        low = 10 ** (n - 1)
        
        # Generate palindrome by mirroring the first half
        for left in range(high, low - 1, -1):
            # Create palindrome from 'left' like: 99 -> 9009
            s = str(left)
            pal = int(s + s[::-1])
            
            # Check if pal can be expressed as a * b where both have n digits
            for i in range(high, low - 1, -1):
                if pal // i > high:
                    break  # If the other factor is more than 'high', skip
                if pal % i == 0:
                    return pal % 1337  # Found it!

        return -1  # Fallback (should never reach here)
