from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        @lru_cache(None)
        def solve(i,j):
            if i >= m or j>=n:
                return 0
            maxi = 1
            for dr,dc in dirs:
                nr,nc = i+dr,j+dc
                if 0<=nr<m and 0<=nc<n and matrix[i][j] < matrix[nr][nc]:
                    maxi = max(maxi,1 + solve(nr,nc))
            return maxi
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans,solve(i,j))
        
        return ans

            