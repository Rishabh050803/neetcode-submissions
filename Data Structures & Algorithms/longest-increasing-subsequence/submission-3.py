from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def solve(prev, curr):
            if curr >= n:
                return 0
            ans = solve(prev, curr + 1)
            if prev == -1 or nums[prev] < nums[curr]:
                ans = max(ans, 1 + solve(curr, curr + 1))

            return ans

        return solve(-1, 0)