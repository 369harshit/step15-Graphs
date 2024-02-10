def solve(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(i, j):
        if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
            board[i][j] = 'S'  # Mark the 'O' as safe
            # Explore in all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    # Step 1: Mark 'O's on the border and connected to the border as safe
    for i in range(rows):
        dfs(i, 0)        # Left border
        dfs(i, cols - 1)  # Right border

    for j in range(cols):
        dfs(0, j)        # Top border
        dfs(rows - 1, j)  # Bottom border

    # Step 2: Iterate through the entire matrix and replace remaining 'O's with 'X's
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'

# Example usage:
input_board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

solve(input_board)

for row in input_board:
    print(row)
