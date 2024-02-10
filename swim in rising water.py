import heapq
def swim_in_rising_water(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Helper function to check if a cell is within the grid
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Dijkstra's algorithm
    def dijkstra():
        min_heap = [(grid[0][0], 0, 0)]  # (weight, x, y)
        visited = set()
        max_distance = 0  # Track the maximum distance encountered

        while min_heap:
            weight, x, y = heapq.heappop(min_heap)

            if (x, y) in visited:
                continue

            visited.add((x, y))
            max_distance = max(max_distance, weight)

            if x == rows - 1 and y == cols - 1:
                return max_distance

            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for nx, ny in neighbors:
                if is_valid(nx, ny):
                    heapq.heappush(min_heap, (max(weight, grid[nx][ny]), nx, ny))

    return dijkstra()

# Example usage
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

result = swim_in_rising_water(grid)
print(result)
