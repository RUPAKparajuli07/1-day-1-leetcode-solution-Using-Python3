class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            # Check if it's within the 32-bit signed integer range
            if dividend == -2**31:
                return 2**31 - 1
            return -dividend
        
        # Determine the sign of the result
        neg = (dividend < 0) != (divisor < 0)
        
        # Convert both dividend and divisor to positive
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            # Subtract divisor from dividend until dividend becomes smaller than divisor
            temp_divisor, count = divisor, 1
            while dividend >= temp_divisor:
                dividend -= temp_divisor
                quotient += count
                # Double the divisor and count to speed up the process
                temp_divisor <<= 1
                count <<= 1
        
        # If the result needs to be negative, negate it
        if neg:
            quotient = -quotient
        
        # Ensure the result is within the 32-bit signed integer range
        if quotient < -2**31:
            return -2**31
        if quotient > 2**31 - 1:
            return 2**31 - 1
        
        return quotient

# Example usage:
solution = Solution()
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
