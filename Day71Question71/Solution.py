class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/' to handle each component
        components = path.split('/')
        stack = []

        # Iterate over each component in the path
        for component in components:
            if component == '' or component == '.':
                # Skip empty and current directory components
                continue
            elif component == '..':
                # Go up one directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name, push onto the stack
                stack.append(component)
        
        # Join the stack to form the simplified path
        return '/' + '/'.join(stack)

# Example usage
solution = Solution()
print(solution.simplifyPath("/home/"))               # Output: "/home"
print(solution.simplifyPath("/home//foo/"))          # Output: "/home/foo"
print(solution.simplifyPath("/home/user/Documents/../Pictures")) # Output: "/home/user/Pictures"
print(solution.simplifyPath("/../"))                 # Output: "/"
print(solution.simplifyPath("/.../a/../b/c/../d/./")) # Output: "/.../b/d"
