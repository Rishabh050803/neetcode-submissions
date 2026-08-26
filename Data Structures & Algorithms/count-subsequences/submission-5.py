from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        @lru_cache(None)
        def solve(i,j):
            if j >= n:
                return 1
            if i >= m:
                return 0
            
            ans = 0
            if s[i] == t[j]:
                ans += solve(i+1,j+1)
            ans += solve(i+1,j)
            return ans
        
        return solve(0,0)
