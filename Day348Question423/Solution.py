from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count frequency of each character
        char_count = Counter(s)
        
        # Count occurrences of each digit based on unique characters
        digit_count = {}
        digit_count[0] = char_count['z']  # "zero"
        digit_count[2] = char_count['w']  # "two"
        digit_count[4] = char_count['u']  # "four"
        digit_count[6] = char_count['x']  # "six"
        digit_count[8] = char_count['g']  # "eight"
        
        # Use remaining characters to determine other numbers
        digit_count[1] = char_count['o'] - digit_count[0] - digit_count[2] - digit_count[4]
        digit_count[3] = char_count['h'] - digit_count[8]
        digit_count[5] = char_count['f'] - digit_count[4]
        digit_count[7] = char_count['s'] - digit_count[6]
        digit_count[9] = char_count['i'] - digit_count[5] - digit_count[6] - digit_count[8]
        
        # Construct the output string
        result = []
        for digit in range(10):
            result.append(str(digit) * digit_count.get(digit, 0))
        
        return "".join(result)
