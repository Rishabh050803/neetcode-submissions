from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @lru_cache(None)
        def pow(x,p):
            if p == 0:
                return 1
            if p == 1:
                return x
            
            if p%2:
                return x*pow(x,p//2)*pow(x,p//2)
            return pow(x,p//2)*pow(x,p//2)
        
        if n < 0:
            return 1/pow(x,abs(n))
        
        return pow(x,n)