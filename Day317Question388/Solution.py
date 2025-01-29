class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        stack = [0]  # Initialize stack with base length 0
        
        for line in input.split('\n'):
            depth = line.count('\t')  # Determine the depth of the current line
            name = line.lstrip('\t')  # Remove leading tabs to get the name
            
            # If the current depth is less than the stack size, pop elements
            while depth + 1 < len(stack):
                stack.pop()
            
            if '.' in name:  # It's a file
                max_len = max(max_len, stack[-1] + len(name))
            else:  # It's a directory
                stack.append(stack[-1] + len(name) + 1)  # +1 for the '/'
        
        return max_len
