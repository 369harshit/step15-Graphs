import heapq
def minimumEffortPath(heights):
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue to store (effort, row, col)
    min_heap = [(0, 0, 0)]

    # Set to store visited cells
    visited = set()

    while min_heap:
        effort, row, col = heapq.heappop(min_heap)

        # If we reached the bottom-right cell
        if row == rows - 1 and col == cols - 1:
            return effort

        # Mark current cell as visited
        visited.add((row, col))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                heapq.heappush(min_heap, (new_effort, new_row, new_col))
    return -1

# Example usage
heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]
result = minimumEffortPath(heights)
print(result)
