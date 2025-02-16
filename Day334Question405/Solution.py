class Solution:
    def toHex(self, num: int) -> str:
        # If the number is zero, return "0"
        if num == 0:
            return "0"
        
        # Hexadecimal characters map
        hex_map = "0123456789abcdef"
        
        # Convert negative number to 32-bit unsigned integer
        if num < 0:
            num += 2 ** 32  # Two's complement
        
        hex_str = ""
        
        # Extract 4 bits at a time (because 1 hex digit = 4 bits)
        while num > 0:
            hex_str = hex_map[num & 15] + hex_str  # Get last 4 bits and convert to hex
            num >>= 4  # Shift right by 4 bits
        
        return hex_str
