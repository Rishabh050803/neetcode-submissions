class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        trz = lcz = False # top row setZeroes, left column setZeroes
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    trz = trz or i==0
                    lcz = lcz or j==0
        # print(matrix)
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        # print(matrix)
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        # print(matrix)
        if trz:
            for j in range(n):
                matrix[0][j] = 0
        # print(matrix)
        if lcz:
            for i in range(m):
                matrix[i][0] = 0

        