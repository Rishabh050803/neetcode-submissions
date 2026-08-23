class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2:
            return False
        total = total//2
        
        def solve(curr,target):
            if target == 0:
                return True
            
            if curr >= n and target:
                return False
            
            return solve(curr+1,target-nums[curr]) or solve(curr+1,target)
        
        return solve(0,total)