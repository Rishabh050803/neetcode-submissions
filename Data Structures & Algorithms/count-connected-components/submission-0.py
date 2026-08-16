class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = set()
        adj = defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        def dfs(node):
            nonlocal vis
            if node in vis:
                return
            vis.add(node)
            for x in adj[node]:
                dfs(x)
            return 
        
        cnt = 0
        for x in range(n):
            if x not in vis:
                cnt+=1
                dfs(x)
        return cnt