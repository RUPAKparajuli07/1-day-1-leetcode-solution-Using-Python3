from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Memoization dictionary to store results for sub-expressions
        memo = {}
        
        # Helper function to recursively compute results for each sub-expression
        def compute(expr: str) -> List[int]:
            # If result is already computed, return it from memo
            if expr in memo:
                return memo[expr]
            
            # If expression is just a number, convert it to int and return as single result
            if expr.isdigit():
                return [int(expr)]
            
            results = []
            
            # Divide and conquer around each operator in the expression
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Compute left and right parts
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    # Combine results based on the current operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            
            # Store the computed results in memo for future use
            memo[expr] = results
            return results
        
        # Call the recursive function on the full expression
        return compute(expression)
