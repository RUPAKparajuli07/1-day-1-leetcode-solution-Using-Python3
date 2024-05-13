class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        
        k -= 1
        result = ''
        for i in range(n - 1, -1, -1):
            index = k // (fact // (i + 1))
            result += numbers.pop(index)
            k %= fact // (i + 1)
            fact //= (i + 1)
        
        return result
