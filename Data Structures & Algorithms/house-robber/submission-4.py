class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = curr = 0
        for i in range(n-1,-1,-1):
            temp = max(nums[i]+prev,curr)
            prev = curr
            curr = temp
        return curr