import heapq
def network_delay_time(times, n, k):
    # Create an adjacency list to represent the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Initialize distances with infinity for all nodes except the source
    distances = {}
    for i in range(1, n+1):
        distances[i] = float('inf')
    distances[k] = 0
    
    # Priority queue to keep track of nodes and their distances
    pq = [(0, k)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Check if this path to the current node is better than the known path
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, edge_weight in graph[current_node]:
            new_distance = current_distance + edge_weight
            
            # If a shorter path is found, update the distance and push to the queue
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    
    # If there are still nodes with infinite distance, it means they are unreachable
    for dist in distances.values():        
        if dist == float('inf'):           
            return -1
    
    # Return the maximum distance among all nodes
    return max(distances.values())

# Example usage
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
result = network_delay_time(times, n, k)
print(result)
