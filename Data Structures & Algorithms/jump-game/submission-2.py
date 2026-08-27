class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        for i,x in enumerate(nums):
            if maxi < i:
                return False
            maxi = max(maxi,i+x)
        return maxi >= len(nums) - 1