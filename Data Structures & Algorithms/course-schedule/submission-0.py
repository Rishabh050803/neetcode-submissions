class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vis = [0]*numCourses

        adj = defaultdict(list)
        for t,r in prerequisites:
            adj[r].append(t)
        
        def dfs(node):
            nonlocal vis
            if vis[node] == 1:
                return True
            if vis[node] == 2:
                return False
            vis[node] = 1
            for x in adj[node]:
                if dfs(x):
                    return True
            vis[node] = 2
            return False

        
        for x in range(numCourses):
            if dfs(x):
                return False
        return True