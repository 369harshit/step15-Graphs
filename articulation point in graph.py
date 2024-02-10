from typing import List
class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if not vis[neighbor]:
                self.dfs(neighbor, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] >= tin[node] and parent != -1:
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node], tin[neighbor])
        if child > 1 and parent == -1:
            mark[node] = 1

    def articulation_points(self, n, edges):
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        mark = [0] * n
        adj = []
        for _ in range(n):
            adj.append([])

        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if not vis[i]:
                self.dfs(i, -1, vis, tin, low, mark, adj)

        ans = []
        for i in range(n):
            if mark[i] == 1:
                ans.append(i)
        if not ans:
            return [-1]
        return ans

# Example usage:
n = 7
edges = [[0, 1], [0, 2],[0, 3], [3, 2], [2, 4],[2, 5],[4, 6],[5, 6]]

obj = Solution()
nodes = obj.articulation_points(n, edges)
print("Articulation Points:", nodes)
