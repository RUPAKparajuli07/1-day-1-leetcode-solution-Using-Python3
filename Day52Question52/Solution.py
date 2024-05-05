class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col, queens):
            for r, c in queens:
                if row == r or col == c or abs(row - r) == abs(col - c):
                    return False
            return True
        
        def backtrack(row, queens):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    queens.append((row, col))
                    count += backtrack(row + 1, queens)
                    queens.pop()
            return count
        
        return backtrack(0, [])
