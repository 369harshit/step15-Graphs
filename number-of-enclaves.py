def numEnclaves(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
            grid[i][j] = -1  # Mark as visited

            # Explore in all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    # Step 1: Mark land cells connected to the top and bottom boundaries
    for i in range(rows):
        if grid[i][0] == 1:
            dfs(i, 0)
        if grid[i][cols - 1] == 1:
            dfs(i, cols - 1)

    # Step 2: Mark land cells connected to the left and right boundaries
    for j in range(cols):
        if grid[0][j] == 1:
            dfs(0, j)
        if grid[rows - 1][j] == 1:
            dfs(rows - 1, j)

    # Step 3: Count the remaining unmarked land cells
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1

    return count

# Example usage:
binary_matrix = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

result = numEnclaves(binary_matrix)
print(result)
