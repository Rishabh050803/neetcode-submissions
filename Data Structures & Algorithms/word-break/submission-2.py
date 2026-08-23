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
        
        return solve(0,0)