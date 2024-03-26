class Solution:
    def intToRoman(self, num: int) -> str:
        # Define mappings of integers to Roman numerals
        integer_to_roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        
        # Initialize an empty string to store the Roman numeral representation
        roman_numeral = ""
        
        # Iterate through each integer value and its corresponding Roman numeral
        for value, numeral in integer_to_roman.items():
            # Repeat the current Roman numeral as many times as necessary
            while num >= value:
                roman_numeral += numeral
                num -= value
        
        return roman_numeral

# Test cases
sol = Solution()
print(sol.intToRoman(3))    # Output: "III"
print(sol.intToRoman(58))   # Output: "LVIII"
print(sol.intToRoman(1994)) # Output: "MCMXCIV"
