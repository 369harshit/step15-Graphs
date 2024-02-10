import heapq
def count_shortest_paths(n, roads):
    graph = {}
    
    for i in range(n):
       graph[i] = []
    

    for road in roads:
        u, v, time = road
        graph[u].append((v, time))
        graph[v].append((u, time))

    distances = [float('inf')] * n
    counts = [0] * n

    distances[0] = 0
    counts[0] = 1

    heap = [(0, 0)]  # (distance, node)

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, time in graph[current_node]:
            new_distance = current_distance + time

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                counts[neighbor] = counts[current_node]
                heapq.heappush(heap, (new_distance, neighbor))
            elif new_distance == distances[neighbor]:
                counts[neighbor] += counts[current_node]
                
    return counts[n - 1]

# Example usage:
n = 9
edges = [[0, 1, 1], [0, 2, 2], [0, 3, 1], [0, 4, 2], [1, 5, 2], [2, 5, 1], [3, 5, 2], [3, 7, 3], [3, 6, 2], [4, 6, 1],[5,8,1],[7,8,1],[6,8,1]]
result = count_shortest_paths(n, edges)
print(result)
