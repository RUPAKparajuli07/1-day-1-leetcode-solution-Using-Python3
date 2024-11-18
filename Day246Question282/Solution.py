from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        results = []

        def backtrack(index, expression, prev_operand, current_value):
            # Base case: When the entire string is used
            if index == len(num):
                # Check if the current value matches the target
                if current_value == target:
                    results.append(expression)
                return
            
            # Iterate over possible splits of the remaining string
            for i in range(index, len(num)):
                # Extract the substring for the current operand
                current_str = num[index:i + 1]
                
                # Avoid operands with leading zeros
                if len(current_str) > 1 and current_str[0] == "0":
                    continue
                
                # Convert the current substring to an integer
                current_operand = int(current_str)

                # If this is the first operand, no operator is needed
                if index == 0:
                    backtrack(i + 1, current_str, current_operand, current_operand)
                else:
                    # Addition
                    backtrack(i + 1, expression + "+" + current_str, current_operand, current_value + current_operand)
                    # Subtraction
                    backtrack(i + 1, expression + "-" + current_str, -current_operand, current_value - current_operand)
                    # Multiplication
                    backtrack(
                        i + 1,
                        expression + "*" + current_str,
                        prev_operand * current_operand,
                        current_value - prev_operand + (prev_operand * current_operand),
                    )
        
        # Initiate backtracking from the first character
        backtrack(0, "", 0, 0)
        return results
