def eventualSafeNodes(graph):
    def isSafe(node):
        if colors[node] != 0:
            return colors[node] == 2

        colors[node] = 1  # Mark as visiting

        for neighbor in graph[node]:
            if not isSafe(neighbor):
                return False

        colors[node] = 2  # Mark as visited and safe
        return True

    n = len(graph)
    colors = [0] * n  # 0: not visited, 1: visiting, 2: visited and safe

    result = []
    for i in range(n):
        if isSafe(i):
            result.append(i)

    return result

# Example usage:
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
output = eventualSafeNodes(graph)
print(output)
