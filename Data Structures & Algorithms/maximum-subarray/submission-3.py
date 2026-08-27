class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -float("inf")
        total = 0
        for x in nums:
            total += x
            maxi = max(maxi,total)
            total = max(total,0)
        return maxi