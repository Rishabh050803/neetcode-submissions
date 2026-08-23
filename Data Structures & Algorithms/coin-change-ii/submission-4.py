from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = list(set(coins))
        print(coins)
        n = len(coins)
        @lru_cache(None)
        def solve(i,amt):
            if amt == 0:
                return 1
            if i >= n or amt < 0:
                return 0
            
            return solve(i,amt-coins[i]) + solve(i+1,amt)
        
        return solve(0,amount)