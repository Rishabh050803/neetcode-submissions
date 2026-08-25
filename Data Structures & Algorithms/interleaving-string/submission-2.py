from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n = len(s1),len(s2)
        if m+n != len(s3):
            return False
        @lru_cache
        def solve(i,j):
            if i >= m:
                return s3[i+j:] == s2[j:]
            if j >= n:
                return s3[i+j:] == s1[i:]
            
            if s1[i] == s3[i+j]:
                if solve(i+1,j):
                    return True
            
            if s2[j] == s3[i+j]:
                if solve(i,j+1):
                    return True
            return False
        
        return solve(0,0)