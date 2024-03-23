class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        
        # Reverse the number
        reversed_num = 0
        original_num = x
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Check if the reversed number is equal to the original number
        return original_num == reversed_num
