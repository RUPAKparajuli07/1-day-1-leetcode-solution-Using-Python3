class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator
        if numerator == 0:
            return "0"
        
        # Determine the sign of the result
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        
        # Work with absolute values to avoid negative issues
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Compute the integer part
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        # If no remainder, return the result as integer
        if remainder == 0:
            return sign + str(integer_part)
        
        # Initialize the result with the integer part and the decimal point
        result = [sign + str(integer_part), "."]
        
        # Dictionary to store the remainder and its index in the result list
        remainder_dict = {}
        
        # Compute the decimal part
        while remainder and remainder not in remainder_dict:
            # Store the position of the remainder
            remainder_dict[remainder] = len(result)
            
            # Multiply the remainder by 10 to get the next digit
            remainder *= 10
            result.append(str(remainder // denominator))
            
            # Update the remainder
            remainder %= denominator
        
        # If remainder repeats, insert parentheses
        if remainder in remainder_dict:
            index = remainder_dict[remainder]
            result.insert(index, "(")
            result.append(")")
        
        # Join the result list into a single string
        return "".join(result)
