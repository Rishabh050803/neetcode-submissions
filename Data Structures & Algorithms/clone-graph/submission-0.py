"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dummy = Node(node.val)
        head = dummy
        vis = set()
        mp = defaultdict(Node)
        mp[1] = head
        def dfs(node,dup):
            nonlocal vis,mp
            if not node or node.val in vis:
                return
            vis.add(node.val)
            print(node.val)
            for x in node.neighbors:
                if not x:
                    continue
                if x.val in mp:
                    newx = mp[x.val]
                else:
                    newx = Node(x.val)
                    mp[x.val] = newx
                dup.neighbors.append(newx)
                dfs(x,newx)
            return
        dfs(node,head)
        print(mp)
        return head