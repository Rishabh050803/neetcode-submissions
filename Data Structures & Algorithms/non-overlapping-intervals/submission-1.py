class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        farthest = intervals[0][1]
        n = len(intervals)
        cnt = 0
        # print(intervals)
        for i in range(1,n):
            s,e = intervals[i]
            if farthest > s:
                cnt += 1
            else:
                farthest = max(farthest,e)
        return cnt
