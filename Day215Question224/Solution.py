class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_res,curr_num = 0,0
        sign = 1
        for i in range(len(s)):

            char = s[i]

            if char.isdigit():
                curr_num = curr_num*10+int(char)

            elif char == '+' or char == '-':
                curr_res += curr_num*sign
                sign = 1 if char == '+' else -1
                curr_num = 0

            elif char == '(':
                stack.append((curr_res, sign))
                curr_res = 0
                sign = 1

            elif char == ')':
                curr_res+=sign*curr_num
                prev, p_sign = stack.pop()
                curr_res = prev+curr_res*p_sign
                curr_num = 0

        curr_res += curr_num*sign
        return curr_res

            
