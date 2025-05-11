class Solution:
    def convertToBase7(self, num: int) -> str:
        # Special case for 0
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        result = ""

        # Repeatedly divide the number by 7 and prepend the remainders
        while num > 0:
            result = str(num % 7) + result
            num //= 7
        
        # Add the negative sign if the original number was negative
        return "-" + result if negative else result
