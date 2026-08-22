class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        def solve(curr,n):
            if curr>=n:
                return 0
            return max(nums[curr] + solve(curr+2,n),solve(curr+1,n))
        n = len(nums)

        # return max(solve(0,n-1),solve(1,n))
        dp = [0]*(n+2)
        dp2 = [0]*(n+2)
        maxi = -1
        for i in range(n-1,0,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        for i in range(n-2,-1,-1):
            dp2[i] = max(nums[i]+dp2[i+2],dp2[i+1])
        print(dp)
        return max(dp[1],dp2[0])
        
