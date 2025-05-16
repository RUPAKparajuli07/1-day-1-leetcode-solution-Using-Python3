class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        total = 1  # 1 is a divisor of every number
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:  # Avoid adding the square root twice
                    total += num // i
            i += 1
        
        return total == num
