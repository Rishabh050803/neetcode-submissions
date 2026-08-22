from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(None)
        def solve(step):
            if step == n:
                return 1
            if step > n:
                return 0
            return solve(step + 2) + solve(step + 1)

        # return solve(0)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n, -1,-1):
            if i + 1 <= n:
                # print(i,"c1")
                dp[i] += dp[i + 1]
            if i + 2 <= n:
                # print(i,"c2")
                dp[i] += dp[i + 2]
        print(dp)
        return dp[0]
