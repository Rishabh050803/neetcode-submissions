from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def canFinish(self, chars, graph):
        vis = defaultdict(int)
        ans = []
        def dfs(node):
            if vis[node] == 1:
                return True       
            if vis[node] == 2:
                return False    
            vis[node] = 1
            for x in graph[node]:
                if dfs(x):
                    return True
            vis[node] = 2
            ans.append(node)
            return False
        for ch in chars:
            if dfs(ch):
                return False
        ans.reverse()
        self.ans = ans
        return True

    def foreignDictionary(self, words: List[str]) -> str:
        uniq = set()
        graph = defaultdict(list)
        for word in words:
            for ch in word:
                uniq.add(ch)

        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            j = 0
            while (
                j < len(prev)
                and j < len(curr)
                and prev[j] == curr[j]
            ):
                j += 1

            if j == len(curr) and len(prev) > len(curr):
                return ""

            if j < len(prev) and j < len(curr):
                graph[prev[j]].append(curr[j])

        if not self.canFinish(uniq, graph):
            return ""

        if len(self.ans) != len(uniq):
            return ""

        return "".join(self.ans)