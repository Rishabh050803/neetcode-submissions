class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(curr):
            if curr >= n:
                return 0
            return max(nums[curr] + solve(curr+2),solve(curr+1))
        
        dp = [0]*(n+2)
        for i in range(n-1,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])

        return dp[0]