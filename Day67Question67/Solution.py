class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result string and carry variable
        result = []
        carry = 0
        
        # Pointers for the two strings
        i, j = len(a) - 1, len(b) - 1
        
        # Loop through both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            # If the current digit of 'a' is available, add it to the sum
            if i >= 0:
                carry += int(a[i])
                i -= 1
            
            # If the current digit of 'b' is available, add it to the sum
            if j >= 0:
                carry += int(b[j])
                j -= 1
            
            # Append the current digit to the result
            result.append(str(carry % 2))
            
            # Update the carry (0 or 1)
            carry //= 2
        
        # The result is currently in reverse order, so reverse it
        result.reverse()
        
        # Join the list to form the final binary string
        return ''.join(result)
