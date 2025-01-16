# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n  # Define the search range
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle point
            result = guess(mid)  # Use the guess API
            
            if result == 0:
                return mid  # If the guess is correct, return the number
            elif result == -1:
                right = mid - 1  # Narrow the search range to the left half
            else:  # result == 1
                left = mid + 1  # Narrow the search range to the right half
