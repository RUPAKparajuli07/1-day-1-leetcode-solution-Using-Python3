class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # The optimal product is achieved by breaking the number into as many 3s as possible
        product = 1
        
        # While n is greater than 4, subtract 3 and multiply the product by 3
        while n > 4:
            product *= 3
            n -= 3
        
        # Multiply the remaining n with the product (this will be 2, 3, or 4)
        product *= n
        return product
