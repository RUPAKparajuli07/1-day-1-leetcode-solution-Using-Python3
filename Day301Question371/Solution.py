class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Define a mask to handle overflow for 32-bit integers
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        while b != 0:
            # XOR gives the sum without carry
            sum_without_carry = a ^ b
            # AND followed by left shift gives the carry
            carry = (a & b) << 1
            
            # Apply mask to handle 32-bit overflow
            a = sum_without_carry & MASK
            b = carry & MASK
        
        # If a is greater than INT_MAX, it means it's a negative number in 32-bit
        return a if a <= INT_MAX else ~(a ^ MASK)
