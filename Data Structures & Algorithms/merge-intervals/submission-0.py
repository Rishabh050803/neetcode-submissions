class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        print(intervals)
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            prev_e = ans[-1][1]
            if prev_e >= s:
                ans[-1][1] = max(ans[-1][1],e)
            else:
                ans.append([s,e])
        return ans