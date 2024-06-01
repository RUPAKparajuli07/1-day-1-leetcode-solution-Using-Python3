from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        
        # Helper function for DFS search
        def dfs(x, y, index):
            # If we have checked all characters in the word
            if index == len(word):
                return True
            
            # Check if out of bounds or character does not match
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False
            
            # Temporarily mark the cell as visited
            temp = board[x][y]
            board[x][y] = '#'
            
            # Explore the neighbors (up, down, left, right)
            found = (dfs(x + 1, y, index + 1) or
                     dfs(x - 1, y, index + 1) or
                     dfs(x, y + 1, index + 1) or
                     dfs(x, y - 1, index + 1))
            
            # Restore the cell's original value
            board[x][y] = temp
            
            return found
        
        # Iterate over each cell in the board
        for i in range(m):
            for j in range(n):
                # If the first character matches, start the DFS search
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        # If no path matches the word, return False
        return False

# Example usage:
solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))  # Output: True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))    # Output: True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))   # Output: False
