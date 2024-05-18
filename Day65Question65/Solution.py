import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression to match the valid number format
        number_regex = re.compile(r"""
            ^                           # start of string
            [+-]?                       # optional sign
            (                           # main number part
                (\d+\.\d*) |            # digits followed by dot (with optional digits)
                (\.\d+) |               # dot followed by digits
                (\d+(\.\d*)?)           # digits (with optional dot and more digits)
            )
            ([eE][+-]?\d+)?             # optional exponent part
            $                           # end of string
        """, re.VERBOSE)
        
        # Match the regex pattern to the input string
        return bool(number_regex.match(s))

# Example usage:
solution = Solution()
print(solution.isNumber("0"))        # Output: True
print(solution.isNumber("e"))        # Output: False
print(solution.isNumber("."))        # Output: False
print(solution.isNumber("2e10"))     # Output: True
print(solution.isNumber("-90E3"))    # Output: True
print(solution.isNumber("1e"))       # Output: False
print(solution.isNumber("e3"))       # Output: False
print(solution.isNumber("99e2.5"))   # Output: False
print(solution.isNumber("--6"))      # Output: False
print(solution.isNumber("-+3"))      # Output: False
print(solution.isNumber("95a54e53")) # Output: False
