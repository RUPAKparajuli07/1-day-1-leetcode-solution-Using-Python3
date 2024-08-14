from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables
        max_product = nums[0]  # This will hold the maximum product found
        min_product = nums[0]  # This will hold the minimum product found
        result = nums[0]  # This will store the overall maximum product

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]

            # If num is negative, it swaps max and min products
            if num < 0:
                max_product, min_product = min_product, max_product

            # Update the max and min products
            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)

            # Update the result with the maximum product found so far
            result = max(result, max_product)

        return result
