from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                # Pop the top two elements from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation and push the result back onto the stack
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Perform integer division that truncates towards zero
                    stack.append(int(a / b))
            else:
                # Token is an operand, push it onto the stack
                stack.append(int(token))
        
        # The final result is the only element left in the stack
        return stack[0]
