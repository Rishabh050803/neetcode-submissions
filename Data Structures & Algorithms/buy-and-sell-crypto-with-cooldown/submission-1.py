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
        
        return solve(0,True)

        