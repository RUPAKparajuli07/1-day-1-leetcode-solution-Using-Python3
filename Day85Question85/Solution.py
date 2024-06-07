from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        # Dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize heights array
        heights = [0] * cols
        
        max_area = 0
        
        for row in matrix:
            for i in range(cols):
                # Update the current histogram height
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate the maximum area for the current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Append a zero height to ensure the last actual bar is processed
        
        for i in range(len(heights)):
            # Maintain a non-decreasing stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # If stack is empty, it means the popped bar is the smallest bar up to i
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        heights.pop()  # Restore the original heights list
        return max_area
