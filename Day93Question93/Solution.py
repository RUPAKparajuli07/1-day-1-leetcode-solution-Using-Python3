from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            # Check if the segment is between 0 and 255 and has no leading zeros
            return 0 <= int(segment) <= 255 and (segment == "0" or not segment.startswith("0"))
        
        def backtrack(start: int, path: List[str]):
            # If we have 4 segments and are at the end of the string, it's a valid IP address
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            
            # Try to place a dot after each of the next three characters
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])
        
        result = []
        backtrack(0, [])
        return result

# Example usage:
sol = Solution()
print(sol.restoreIpAddresses("25525511135"))  # Output: ["255.255.11.135","255.255.111.35"]
print(sol.restoreIpAddresses("0000"))        # Output: ["0.0.0.0"]
print(sol.restoreIpAddresses("101023"))      # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
