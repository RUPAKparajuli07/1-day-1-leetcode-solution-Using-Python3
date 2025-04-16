class Solution:
    def findComplement(self, num: int) -> int:
        # Get the number of bits in num
        bit_length = num.bit_length()
        
        # Create a bitmask with all bits set to 1 for the length of num
        mask = (1 << bit_length) - 1
        
        # XOR num with mask to get the complement
        return num ^ mask
