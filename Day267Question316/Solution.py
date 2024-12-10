class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Step 1: Track the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Step 2: Initialize the stack and visited set
        stack = []
        visited = set()
        
        # Step 3: Iterate through the string
        for idx, char in enumerate(s):
            # Skip if the character is already in the stack
            if char in visited:
                continue
            
            # Ensure the stack maintains the lexicographically smallest order
            while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                removed = stack.pop()
                visited.remove(removed)  # Mark it as not visited
            
            # Add the current character to the stack and mark it as visited
            stack.append(char)
            visited.add(char)
        
        # Step 4: Convert the stack into a string and return
        return ''.join(stack)
