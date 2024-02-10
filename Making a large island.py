from collections import deque
def largest_connected_group(grid):
    n = len(grid)
    max_group_size = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(i, j):
        visited = set()
        count = 0
        queue = deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            count += 1

            for dx, dy in directions:
                ni, nj = x + dx, y + dy
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) not in visited:
                    queue.append((ni, nj))

        return count

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1
                max_group_size = max(max_group_size, bfs(i, j))
                grid[i][j] = 0  # Backtrack

    return max_group_size

# Example Usage:
grid = [
        [1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0]
    ]

result = largest_connected_group(grid)
print(result)
