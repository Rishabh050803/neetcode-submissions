from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        @lru_cache(None)
        def solve(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
            cnt = 0
            # 1 char
            if s[curr] == '0':
                return 0
            cnt = solve(curr+1)
            if curr + 1 >=n:
                return cnt
            if int(s[curr:curr+2]) <= 26:
                cnt += solve(curr+2)
            
            return cnt
        return solve(0)