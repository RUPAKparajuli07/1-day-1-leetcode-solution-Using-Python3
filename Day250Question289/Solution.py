class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = {}
        for i in range(len(board)):
            for j in range(len(board[0])):

                cells = [
                            board[i-1][j] if i-1 >= 0 else None, 
                            board[i][j-1] if j-1 >= 0 else None, 
                            board[i+1][j] if i+1 < len(board) else None, 
                            board[i][j+1] if j+1 < len(board[0]) else None, 
                            board[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else None, 
                            board[i+1][j+1] if i+1 < len(board) and j+1 < len(board[0]) else None, 
                            board[i-1][j+1] if i-1 >= 0 and j+1 < len(board[0]) else None, 
                            board[i+1][j-1] if i+1 < len(board) and j-1 >= 0 else None
                        ]

                cells = Counter(cells)
                d[(i,j)] = cells
        for x in d:
            if board[x[0]][x[1]] == 0:
                if d[x][1] == 3:
                    board[x[0]][x[1]] = 1
            else:
                if d[x][1] < 2:
                    board[x[0]][x[1]] = 0
                elif 2 <= d[x][1] <= 3:
                    board[x[0]][x[1]] = 1
                elif d[x][1] > 3:
                    board[x[0]][x[1]] = 0
