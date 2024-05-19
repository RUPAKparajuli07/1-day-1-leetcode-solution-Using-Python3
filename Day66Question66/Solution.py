from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the digits from the last to the first
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, it becomes 0 and carry over 1
            digits[i] = 0
        
        # If all digits were 9, we have a carry-over to add a new most significant digit
        return [1] + digits

# Example usage:
# sol = Solution()
# print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
# print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
# print(sol.plusOne([9]))  # Output: [1,0]
