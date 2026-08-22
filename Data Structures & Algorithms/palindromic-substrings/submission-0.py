class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            l,r = i,i
            
            while l>=0 and r<n and s[l] == s[r]:
                cnt+=1
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l] == s[r]:
                cnt+=1
                l-=1
                r+=1
        return cnt
        