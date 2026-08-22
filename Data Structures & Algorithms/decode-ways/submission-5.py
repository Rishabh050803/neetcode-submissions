class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0

        dp = [0]*(n+2)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            cnt = 0
            if s[i] == '0':
                dp[i] = 0
                continue
            cnt = dp[i+1]
            if i+1 >= n:
                dp[i] = cnt
                continue
            if int(s[i:i+2]) <= 26:
                cnt += dp[i+2]
            dp[i] = cnt
        return dp[0]

            