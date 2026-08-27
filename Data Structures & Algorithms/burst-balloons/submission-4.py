from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # print(nums,n)
        @lru_cache(None)
        def solve(i,j):
            if j >= n or i<0:
                return 1
            
            if i==j:
                return nums[i]
            
            ans = 0
            maxi = 0
            for k in range(i+1,j):
                maxi = nums[i]*nums[j]*nums[k] + solve(i,k)+solve(k,j)
                # print(i,k,j,maxi)
                ans = max(ans, maxi)
            
            return ans
        
        return solve(0,n-1)