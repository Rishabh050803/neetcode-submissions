class Solution:
    def longestPalindrome(self, s: str) -> str:
        #odd len
        b = 0
        maxi = 0
        n = len(s)

        for i in range(n):
            l,r = i,i
            
            while l>=0 and r<n and s[l] == s[r]:
                if maxi < r-l+1:
                    b = l
                    maxi = r-l+1
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l] == s[r]:
                if maxi < r-l+1:
                    b = l
                    maxi = r-l+1
                l-=1
                r+=1
        print(b,maxi)
        return s[b:b+maxi]