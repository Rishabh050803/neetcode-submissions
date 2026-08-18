from functools import lru_cache
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        low, high = 0, n**2 - 1
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        # @lru_cache(None)
        def possible(l):
            visited = [[False] * n for _ in range(n)]
            def dfs(r, c):
                if r < 0 or r >= n or c < 0 or c >= n:
                    return False

                if visited[r][c] or grid[r][c] > l:
                    return False

                if r == n - 1 and c == n - 1:
                    return True

                visited[r][c] = True

                for dr, dc in dirs:
                    if dfs(r + dr, c + dc):
                        return True
                return False
            return dfs(0, 0)
        ans = high
        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans