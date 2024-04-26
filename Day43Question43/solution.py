class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]
                
                result[pos1] += total // 10
                result[pos2] = total % 10
        
        # Convert result to string
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        return ''.join(map(str, result[start:]))
