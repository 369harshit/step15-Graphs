from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

def make_connected(graph):
    visited = [False] * graph.vertices
    components = 0

    for i in range(graph.vertices):
        if not visited[i]:
            components += 1
            graph.dfs(i, visited)

    # The number of operations required is equal to the number of components minus 1
    operations_required = components - 1
    return operations_required

# Example input
N = 9
edges = [[0,1],[0,2],[0,3],[1,2],[2,3],[4,5],[5,6],[7,8]]

g = Graph(N)
for edge in edges:
    g.add_edge(edge[0], edge[1])

operations = make_connected(g)
print("Number of operations required:",operations)
