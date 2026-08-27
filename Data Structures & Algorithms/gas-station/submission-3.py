class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t=c=0
        curr = 0
        n = len(gas)
        start = 0
        for i in range(n):
            t+=gas[i]
            c+=cost[i]
            curr += (gas[i]-cost[i])
            if curr < 0:
                start = (i+1)%n
                curr = 0
        
        if t >= c:
            return start
        return -1