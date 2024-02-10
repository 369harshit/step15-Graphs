import heapq
def findCheapestPrice(n, flights, src, dst, k):
    # Create a graph representation using a dictionary
    graph = {}
    for u, v, w in flights:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    # Priority queue to store (cost, node, stops)
    min_heap = [(0, src, 0)]

    while min_heap:
        cost, node, stops = heapq.heappop(min_heap)

        # If the destination is reached, return the cost
        if node == dst:
            return cost

        # If the number of stops is within the limit
        if stops <= k:
            # Explore neighbors
            if node in graph:
                for neighbor, edge_cost in graph[node]:
                    heapq.heappush(min_heap, (cost + edge_cost, neighbor, stops + 1))

    # If the destination cannot be reached within k stops, return -1
    return -1

# Example usage
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

output = findCheapestPrice(n, flights, src, dst, k)
print(output)
