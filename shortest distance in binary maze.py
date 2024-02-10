from collections import deque
def shortestDistanceBinaryMaze(grid, src, dest):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(src[0], src[1], 0)])  # (row, col, distance)
    visited = set()

    while queue:
        row, col, distance = queue.popleft()
        if (row, col) == (dest[0], dest[1]):
            return distance
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    return -1

# Example usage:
grid = [    [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 1]]

source = (0, 1)
destination = (2, 2)
result = shortestDistanceBinaryMaze(grid, source, destination)
print("Shortest distance:", result)
