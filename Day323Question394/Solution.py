class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Stack to store characters and numbers
        curr_num = 0  # Current number before opening bracket
        curr_str = ""  # Current string being built
        
        for char in s:
            if char.isdigit():
                # If it's a number, update curr_num
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push the current string and number to stack
                stack.append((curr_str, curr_num))
                curr_str = ""  # Reset current string
                curr_num = 0  # Reset current number
            elif char == ']':
                # Pop from stack and repeat the string
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                # Append normal characters to current string
                curr_str += char
        
        return curr_str

# Example test cases
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(sol.decodeString("3[a2[c]]"))   # Output: "accaccacc"
print(sol.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"

