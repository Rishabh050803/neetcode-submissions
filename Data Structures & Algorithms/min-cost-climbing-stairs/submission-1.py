from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def solve(curr):
            if curr >= len(cost):
                return 0
            
            c = cost[curr]

            return c + min(solve(curr+1),solve(curr+2))
        
        return min(solve(0),solve(1))