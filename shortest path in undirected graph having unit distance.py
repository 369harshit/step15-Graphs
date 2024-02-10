from collections import deque

def shortest_paths(n, edges, src):
    graph = {}
    for i in range(n):
        graph[i] = []


    # Build the adjacency list
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    # Initialize distances with -1 (unreachable)
    distances = [-1] * n
    distances[src] = 0

    # Use BFS to find shortest paths
    queue = deque([src])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    return distances


n = 9
m = 10
edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src = 0

result = shortest_paths(n, edges, src)
print("Shortest paths from source (", src, "):", result)
