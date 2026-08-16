class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = [0]*numCourses

        adj = defaultdict(list)
        for t,r in prerequisites:
            adj[r].append(t)
        
        order = []
        
        def dfs(node):
            nonlocal vis,order
            if vis[node] == 1:
                return True
            if vis[node] == 2:
                return False
            vis[node] = 1
            for x in adj[node]:
                if dfs(x):
                    return True
            vis[node] = 2
            order.append(node)
            return False

        
        for x in range(numCourses):
            if dfs(x):
                return []
        order.reverse()
        return order