class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1  # First element
        step = 1  # Difference between elements
        left = True  # Direction flag
        remaining = n  # Elements left
        
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step  # Move head when removing from left or odd count in right
            
            remaining //= 2  # Reduce remaining count
            step *= 2  # Double step size
            left = not left  # Flip direction
        
        return head
