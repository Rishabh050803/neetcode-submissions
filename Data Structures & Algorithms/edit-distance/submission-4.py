from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        @lru_cache(None)
        def solve(r,c):
            if r >= m or c>= n:
                return max(0,abs(r-m),abs(c-n))
                
            if word1[r] == word2[c]:
                return solve(r+1,c+1)
            return 1+min(solve(r+1,c),solve(r,c+1),solve(r+1,c+1))
        
        return solve(0,0)
            