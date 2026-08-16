class DSU:
    def __init__(self,points) -> None:
        self.parent = dict()
        self.rank = dict()
        for point in points:
            self.parent[tuple(point)] = tuple(point)
            self.rank[tuple(point)] = 1

    def getp(self,point):
        point = tuple(point)
        if self.parent[point] == point:
            return point
        self.parent[point] = self.getp(self.parent[point])
        return self.parent[point]
        
    def ubr(self,p1,p2):
        p1,p2 = tuple(p1),tuple(p2)
        p1p = self.getp(p1)
        p2p = self.getp(p2)
        if p1p == p2p:
            return
        if self.rank[p1p] > self.rank[p2p]:
            self.parent[p2p] = p1p
        elif self.rank[p1p] < self.rank[p2p]:
            self.parent[p1p] = p2p
        else:
            self.parent[p2p] = p1p
            self.rank[p1p]+=1
        return

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for x1,y1 in points:
            for x2,y2 in points:
                edges.append([abs(x1-x2) + abs(y1-y2),(x1,y1),(x2,y2)])
            
        ans = 0
        edges.sort()
        dsu = DSU(points)
        print(dsu.parent)
        for wt,p1,p2 in edges:
            if dsu.getp(p1) == dsu.getp(p2):
                continue
            ans+=wt
            dsu.ubr(p1,p2)
        return ans


