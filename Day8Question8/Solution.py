class Solution:
    def myAtoi(self, s: str) -> int:
        # Ignoring leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Checking for sign
        sign = 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Converting digits
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Clamping to 32-bit signed integer range
        num *= sign
        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num

# Example usage:
solution = Solution()
print(solution.myAtoi("42")) # Output: 42
print(solution.myAtoi("   -42")) # Output: -42
print(solution.myAtoi("4193 with words")) # Output: 4193
