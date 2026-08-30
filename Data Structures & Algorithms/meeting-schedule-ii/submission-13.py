"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x.start)
        farthest = intervals[0].end
        n = len(intervals)
        cnt = 0
        heap = [farthest]
        for i in range(1,n):
            s,e = intervals[i].start,intervals[i].end
            if heap[0] > s:
                cnt+=1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap,e)
        return cnt + 1
