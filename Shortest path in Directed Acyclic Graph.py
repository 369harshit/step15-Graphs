from collections import defaultdict
def dfs(graph, node, visited, stack):
    visited[node] = True

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)

    stack.append(node)

def shortest_path_dag(N, edges):
    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))

    visited = [False] * N
    stack = []

    for i in range(N):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    dist = [float('inf')] * N
    dist[0] = 0

    while stack:
        node = stack.pop()
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight

    return dist

# Example
N = 6
edges = [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]
result = shortest_path_dag(N, edges)

# Print the result
for i in range(N):
    print(result[i], end=" ")
