from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Define the mapping of digits to letters
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Helper function to generate combinations
        def backtrack(index, path):
            if index == len(digits):
                combinations.append(''.join(path))
                return
            for letter in digit_map[digits[index]]:
                backtrack(index + 1, path + [letter])
        
        combinations = []
        backtrack(0, [])
        return combinations

# Test the solution
solution = Solution()
print(solution.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations(""))    # Output: []
print(solution.letterCombinations("2"))   # Output: ["a","b","c"]
