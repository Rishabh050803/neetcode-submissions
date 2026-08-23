from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def solve(i,buy):
            if i>=n:
                return 0
            if not buy:
                return max(prices[i] + solve(i+2,True),solve(i+1,False))
            return max(-prices[i]+solve(i+1,False),solve(i+1,True))
        # return solve(0,True)

        dp = [[0,0] for _ in range(n+2)]

        for i in range(n-1,-1,-1):
            dp[i][0] = max(prices[i] + dp[i+2][1],dp[i+1][0])
            dp[i][1] = max(-prices[i] + dp[i+1][0],dp[i+1][1])
        
        return dp[0][1]
