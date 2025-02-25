class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for num1 and num2
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Loop until both strings are processed
        while i >= 0 or j >= 0 or carry:
            # Get the current digits, or 0 if the pointer is out of bounds
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Add digits and carry
            total = digit1 + digit2 + carry
            result.append(str(total % 10))  # Append the current digit (total % 10)
            carry = total // 10  # Update the carry (total // 10)
            
            # Move the pointers
            i -= 1
            j -= 1

        # Reverse the result to get the correct order
        return ''.join(result[::-1])

