class DSU:
    def __init__(self,n) -> None:
        self.parent = []
        self.rank = [1]*n
        for i in range(n):
            self.parent.append(i)
    
    def getp(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.getp(self.parent[x])
        return self.parent[x]

    def ubr(self,x,y):
        xp = self.getp(x)
        yp = self.getp(y)

        if xp == yp:
            return

        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            self.rank[xp]+=1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for x,y in edges:
            n = max(n,x,y)
        
        dsu = DSU(n)
        for x,y in edges:
            if dsu.getp(x-1) == dsu.getp(y-1):
                return [x,y]
            dsu.ubr(x-1,y-1)
        return []