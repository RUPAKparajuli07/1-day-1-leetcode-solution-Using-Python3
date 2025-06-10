class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Helper function to parse a complex number string into real and imaginary parts
        def parse_complex(s):
            real, imag = s.split('+')
            return int(real), int(imag[:-1])  # remove 'i' from the imaginary part
        
        # Parse both numbers
        a, b = parse_complex(num1)
        c, d = parse_complex(num2)
        
        # Apply complex multiplication formula
        real_part = a * c - b * d
        imag_part = a * d + b * c
        
        return f"{real_part}+{imag_part}i"
