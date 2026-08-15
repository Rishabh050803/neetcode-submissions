class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        R, C = len(grid), len(grid[0])
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j,0))
                elif grid[i][j] == 1:
                    fresh+=1
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        timer = 0
        while q:
            print(q)
            r, c, timer = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nc >= 0 and nr < R and nc < C and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append((nr, nc,timer+1))
        print(grid,fresh)
        if fresh:
            return -1
        return timer
