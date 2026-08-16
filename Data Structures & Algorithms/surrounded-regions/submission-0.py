class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        R,C = len(board),len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or board[r][c]!='O':
                return
            board[r][c] = 'V'
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
            return
        
        for i in range(R):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][C-1] == 'O':
                dfs(i,C-1)
        for j in range(C):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[R-1][j] == 'O':
                dfs(R-1,j)
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
    