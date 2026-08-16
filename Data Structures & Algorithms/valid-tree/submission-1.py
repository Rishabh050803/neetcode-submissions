class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        used = []
        vis = set()
        def dfs(x,p):
            nonlocal vis,used
            if x in vis:
                return 
            vis.add(x)
            if p!=-1:
                used.append([min(x,p),max(x,p)])
            for n in adj[x]:
                dfs(n,x)
            return
        dfs(0,-1)
        if len(vis) != n:
            return False
        
        return len(used) == len(edges)
