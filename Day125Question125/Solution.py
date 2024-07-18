class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered list of characters is equal to its reverse
        return filtered_chars == filtered_chars[::-1]

# Example usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(solution.isPalindrome("race a car"))  # Output: false
print(solution.isPalindrome(" "))  # Output: true
