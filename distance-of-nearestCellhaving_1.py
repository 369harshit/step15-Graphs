from collections import deque
def nearest_distance(grid):
    if not grid or not grid[0]:
        return []

    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    def bfs(i, j):
        visited = set()
        queue = deque([(i, j, 0)])

        while queue:
            cur_i, cur_j, dist = queue.popleft()

            if grid[cur_i][cur_j] == 1:
                result[i][j] = dist
                return

            for di, dj in directions:
                ni, nj = cur_i + di, cur_j + dj
                if is_valid(ni, nj) and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append((ni, nj, dist + 1))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                bfs(i, j)

    return result

# Example usage:
binary_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

result_distances = nearest_distance(binary_grid)
for row in result_distances:
    print(row)
