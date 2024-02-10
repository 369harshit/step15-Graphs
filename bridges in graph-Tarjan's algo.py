from typing import List
class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if vis[neighbor] == 0:
                self.dfs(neighbor, node, vis, adj, tin, low, bridges)
                low[node] = min(low[neighbor], low[node])
                # node --- neighbor
                if low[neighbor] > tin[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], low[neighbor])

    def criticalConnections(self, n, connections):
        adj = []
        for _ in range(n):
            adj.append([])
        for connection in connections:
            u, v = connection
            adj[u].append(v)
            adj[v].append(u)
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges

# Example usage:
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

obj = Solution()
bridges = obj.criticalConnections(n, connections)
for bridge in bridges:
   print(f"[{bridge[0]}, {bridge[1]}]", end=" ")
print()
