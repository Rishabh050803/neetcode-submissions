class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        R,C = len(heights),len(heights[0])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(r,c,ocean):
            ocean.add((r,c))
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                
                    dfs(nr,nc,ocean)
            return
        
        for r in range(R):
            dfs(r,0,pacific)
            dfs(r,C-1,atlantic)
        
        for j in range(C):
            dfs(0,j,pacific)
            dfs(R-1,j,atlantic)
        return list(pacific & atlantic)