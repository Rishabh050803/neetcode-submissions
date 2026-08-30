class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.sort()
        if not intervals:
            return [newInterval]
        n = len(intervals)
        for i,[s,e] in enumerate(intervals):
            if newInterval[0] < s:
                intervals.insert(i,newInterval)
                break 
        if n == len(intervals):
            intervals.append(newInterval)
        ans = [intervals[0]]
        
        # print(intervals)
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            prev_e = ans[-1][1]
            if prev_e >= s:
                ans[-1][1] = max(ans[-1][1],e)
            else:
                ans.append([s,e])
        return ans