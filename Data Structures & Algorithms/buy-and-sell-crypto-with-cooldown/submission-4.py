from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr_sell = prev_sell = 0 # (dp[i+1][0],dp[i+2][0])
        curr_buy = prev_buy = 0   # (dp[i+1][1],dp[i+2][1])

        for i in range(n-1,-1,-1):
            temp_sell = max(prices[i] + prev_buy,curr_sell)
            temp_buy = max(-prices[i] + curr_sell,curr_buy)

            prev_sell = curr_sell
            prev_buy = curr_buy
            curr_sell = temp_sell
            curr_buy = temp_buy
        
        return curr_buy
