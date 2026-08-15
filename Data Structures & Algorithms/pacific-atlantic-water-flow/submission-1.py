class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights),len(heights[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        reach = [[[False, False] for _ in range(C)] for _ in range(R)]

        def solve(r,c):
            nonlocal vis
            if (r,c) in vis:
                return reach[r][c]
            vis.add((r,c))
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr >=0 and nc >= 0 and nr < R and nc < C and heights[nr][nc] <= heights[r][c]:
                    p,a = solve(nr,nc)
                    # print(r,c,nr,nc,p,a)
                    reach[r][c][0] = reach[r][c][0] or p
                    reach[r][c][1] = reach[r][c][1] or a
            return reach[r][c]
        
        for i in range(R):
            reach[i][0][0] = True
            reach[i][C-1][1] = True
        for j in range(C):
            reach[0][j][0] = True
            reach[R-1][j][1] = True 
        for i in range(R):
            for j in range(C):
                vis = set()
                reach[i][j] = solve(i,j)
        ans = []
        # for row in reach:
            # print(row)
        for i in range(R):
            for j in range(C):
                
                if reach[i][j][0] and reach[i][j][1]:
                    ans.append((i,j))
        return ans