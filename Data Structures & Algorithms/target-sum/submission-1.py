from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def solve(i,target):
            if i>=n:
                return 1 if target == 0 else 0
            
            return solve(i+1,target-nums[i]) + solve(i+1,target+nums[i])
        
        return solve(0,target)