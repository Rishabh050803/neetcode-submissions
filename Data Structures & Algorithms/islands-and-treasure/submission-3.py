from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        inf = 2147483647
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == inf):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))