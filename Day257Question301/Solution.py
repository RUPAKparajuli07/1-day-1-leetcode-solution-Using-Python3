from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        # Function to check if a string has balanced parentheses
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        # BFS to find the minimum removal of parentheses
        queue = deque([s])
        visited = set([s])
        found_valid = False
        result = []
        
        while queue:
            current_str = queue.popleft()
            
            # If current string is valid, collect it in the result
            if isValid(current_str):
                found_valid = True
                result.append(current_str)
            
            # If we've already found valid strings, stop further exploration
            if found_valid:
                continue
            
            # Generate all possible states by removing one parenthesis at a time
            for i in range(len(current_str)):
                if current_str[i] not in ['(', ')']:
                    continue
                next_str = current_str[:i] + current_str[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        
        return result
