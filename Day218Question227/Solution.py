class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # To hold intermediate results
        current_num = 0
        current_op = '+'  # Default operator
        s = s.replace(" ", "")  # Remove spaces
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Forming the full number
            if char in "+-*/" or i == len(s) - 1:  # End of a number or end of string
                if current_op == '+':
                    stack.append(current_num)
                elif current_op == '-':
                    stack.append(-current_num)
                elif current_op == '*':
                    stack.append(stack.pop() * current_num)
                elif current_op == '/':
                    stack.append(int(stack.pop() / current_num))  # Truncate division toward zero
                current_op = char  # Update current operator
                current_num = 0  # Reset number for the next round
        
        return sum(stack)  # Sum up all numbers in the stack
