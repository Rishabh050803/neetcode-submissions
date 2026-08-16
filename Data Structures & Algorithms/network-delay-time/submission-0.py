class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = math.inf
        dist = [inf]*(n+1)
        dist[k] = 0
        pq = []
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        pq.append([0,k])
        while pq:
            t,v = heapq.heappop(pq)
            for x,t1 in adj[v]:
                if dist[x] > t + t1:
                    heapq.heappush(pq,[t+t1,x])
                    dist[x] = t1 + t

        for i in range(1,n+1):
            if dist[i] == inf:
                return -1
        
        return int(max(dist[1:]))