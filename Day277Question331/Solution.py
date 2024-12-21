class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Split the string into nodes
        nodes = preorder.split(',')
        slots = 1  # Initial slot for the root
        
        for node in nodes:
            slots -= 1  # Consume one slot for the current node
            
            if slots < 0:  # If slots go negative, it's invalid
                return False
            
            if node != '#':  # Non-null nodes create 2 new slots
                slots += 2
        
        # Valid if all slots are used up exactly
        return slots == 0
