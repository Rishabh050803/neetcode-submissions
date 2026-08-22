class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        def solve(curr,amt):
            if amt < 0 or (curr>=n and amt != 0):
                return float("inf")
            if amt == 0:
                return 0
            take = 1 + solve(curr,amt-coins[curr])
            nottake = solve(curr+1,amt)
            return min(take,nottake)
        
        # x = solve(0,amount)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(1,amount+1):
            dp[n][i] = float("inf")
        
        for i in range(n-1,-1,-1):
            for amt in range(0,amount+1):
                if amt >= coins[i]:
                    dp[i][amt] = min(
                        1 + dp[i][amt - coins[i]],
                        dp[i + 1][amt]
                    )
                else:
                    dp[i][amt] = dp[i + 1][amt]
        if dp[0][amount] == float("inf"):
            return -1
        return dp[0][amount]