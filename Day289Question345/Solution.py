class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels
        vowels = set('aeiouAEIOU')
        # Convert the string to a list for easy swapping
        s_list = list(s)
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            # Move pointers
            left += 1
            right -= 1
        
        # Join the list back into a string
        return ''.join(s_list)
