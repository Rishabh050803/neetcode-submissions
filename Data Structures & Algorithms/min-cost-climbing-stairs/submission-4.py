from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [0]*(n+2)
        curr = 0
        prev = 0
        for i in range(n-1,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
            temp = cost[i] + min(prev,curr)
            prev = curr
            curr = temp
        # return min(dp[0],dp[1])
        return min(curr,prev)