class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        adj = defaultdict(list)
        for f,t in tickets:
            adj[f].append(t)
        for k,v in adj.items():
            adj[k] = sorted(v,reverse=True)
        
        ans = []
        print(adj)
        def dfs(s):
            while adj[s]:
                nxt = adj[s].pop()
                dfs(nxt)
            ans.append(s)
        dfs("JFK")
        return ans[::-1]
