from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def solve(curr):
            if curr >= len(cost):
                return 0
            
            c = cost[curr]

            return c + min(solve(curr+1),solve(curr+2))
        
        # return min(solve(0),solve(1))
        n = len(cost)
        dp = [0]*(n+2)
        # dp[n] = 0
        for i in range(n-1,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])