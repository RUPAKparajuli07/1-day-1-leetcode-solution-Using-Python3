class Solution:
    def reverse(self, x: int) -> int:
        # Handle sign separately
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        # Convert integer to string, reverse, and convert back to integer
        reversed_x = int(str(x)[::-1]) * sign
        
        # Check if reversed integer is within 32-bit range
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        else:
            return reversed_x

# Example usage:
solution = Solution()
print(solution.reverse(123))  # Output: 321
print(solution.reverse(-123)) # Output: -321
print(solution.reverse(120))  # Output: 21
