from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def solve(step):
            if step == n:
                return 1
            if step > n:
                return 0
            return solve(step+2) + solve(step+1)
        return solve(0)