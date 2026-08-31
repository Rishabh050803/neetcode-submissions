class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(n//2):
            # print(i)
            for r in range(j,n-j-1):
                # nxt = {prev_column,n-1-prev_rpw}
                nxt_row=j
                nxt_col = n-1-r
                # print(r,i)
                temp = matrix[r][j]
                for i in range(4):
                    # print(f"shifting {temp} to {nxt_row,nxt_col}")
                    t = matrix[nxt_row][nxt_col]
                    matrix[nxt_row][nxt_col] = temp
                    temp = t
                    t = nxt_row 
                    nxt_row=nxt_col
                    nxt_col = (n-1-t )%n
    