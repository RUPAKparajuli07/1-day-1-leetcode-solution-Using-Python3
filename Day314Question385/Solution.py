class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # If the string represents a single integer, return it as a NestedInteger
        if s[0] != '[':
            return NestedInteger(int(s))

        # Initialize a stack to manage nested structures
        stack = []
        current = None
        num = ''
        
        for char in s:
            if char == '[':
                # Push the current NestedInteger to stack and start a new one
                if current:
                    stack.append(current)
                current = NestedInteger()
            elif char == ']':
                # Finish the current NestedInteger
                if num:
                    current.add(NestedInteger(int(num)))
                    num = ''
                if stack:
                    parent = stack.pop()
                    parent.add(current)
                    current = parent
            elif char == ',':
                # If a number exists, add it to the current NestedInteger
                if num:
                    current.add(NestedInteger(int(num)))
                    num = ''
            else:
                # Build the number
                num += char

        return current
