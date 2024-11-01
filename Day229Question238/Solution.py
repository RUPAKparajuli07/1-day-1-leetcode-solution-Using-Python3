from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the answer array with 1s
        answer = [1] * n

        # Left pass: fill answer[i] with the product of all elements to the left of i
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]  # Update the left product for the next position
        
        # Right pass: multiply answer[i] by the product of all elements to the right of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product  # Multiply with the accumulated right product
            right_product *= nums[i]  # Update the right product for the next position
            
        return answer
