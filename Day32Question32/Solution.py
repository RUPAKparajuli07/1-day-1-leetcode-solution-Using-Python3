class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        start_index = -1
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_length = max(max_length, i - stack[-1])
                    else:
                        max_length = max(max_length, i - start_index)
                else:
                    start_index = i
        
        return max_length
