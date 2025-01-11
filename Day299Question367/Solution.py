class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        # Binary search for the square root
        left, right = 2, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            
            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
