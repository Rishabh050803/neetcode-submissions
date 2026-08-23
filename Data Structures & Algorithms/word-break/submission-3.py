from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        @lru_cache(None)
        def solve(curr,start):
            if start>=n:
                return True
            if curr>=n:
                return s[start:curr] in words
            word = s[start:curr+1]
            if word in words:
                if solve(curr+1,curr+1):
                    return True
            return solve(curr+1,start)
        # return solve(0,0)

        dp = [[False]*(n+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][n] = True
            dp[n][i] = s[i:n] in words
        
        for curr in range(n-1,-1,-1):
            for start in range(n-1,-1,-1):
                word = s[start:curr+1]
                if word in words:
                    if dp[curr+1][curr+1]:
                        dp[curr][start] =  dp[curr+1][curr+1]
                        continue

                dp[curr][start] |= dp[curr+1][start]
        
        return dp[0][0]