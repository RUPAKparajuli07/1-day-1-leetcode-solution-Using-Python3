class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        position = 1  # Start from the units place
        
        while position <= n:
            higher = n // (position * 10)
            current = (n // position) % 10
            lower = n % position
            
            if current == 0:
                count += higher * position
            elif current == 1:
                count += higher * position + lower + 1
            else:
                count += (higher + 1) * position
            
            position *= 10  # Move to the next digit position
            
        return count
