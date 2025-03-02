from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0  # Stores maximum XOR found
        mask = 0  # Helps extract prefixes
        
        for i in range(31, -1, -1):  # Check bits from MSB to LSB
            mask |= (1 << i)  # Update mask to consider one more bit
            
            prefixes = set()  # Store all prefixes of numbers
            for num in nums:
                prefixes.add(num & mask)  # Store only the leftmost bits
            
            # Try to form the max XOR by assuming '1' at the current bit
            temp_xor = max_xor | (1 << i)
            
            # Check if there exist two prefixes that can form temp_xor
            for prefix in prefixes:
                if temp_xor ^ prefix in prefixes:  
                    max_xor = temp_xor  # If found, update max_xor
                    break
        
        return max_xor
