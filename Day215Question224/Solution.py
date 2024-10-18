class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        last_operator = '+'
        
        for i in range(len(s)):
            char = s[i]
            
            # If the character is a digit, build the current number
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # If the character is an operator or if it's the last character in the string
            if char in "+-() " or i == len(s) - 1:
                if last_operator == '+':
                    current_result += current_number
                elif last_operator == '-':
                    current_result -= current_number
                elif last_operator == '(':
                    stack.append(current_result)
                    stack.append(last_operator)
                    current_result = 0
                
                # Reset current number for the next number
                current_number = 0
                last_operator = char

                if char == ')':
                    # When we hit a closing parenthesis, we need to pop from the stack
                    last_operator = stack.pop()  # Get the last operator
                    if last_operator == '+':
                        current_result = stack.pop() + current_result
                    elif last_operator == '-':
                        current_result = stack.pop() - current_result
                    # Note: After popping, current_result is now the result up to the previous '('

        return current_result

# Example usage
solution = Solution()
print(solution.calculate("1 + 1"))                # Output: 2
print(solution.calculate(" 2-1 + 2 "))            # Output: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
