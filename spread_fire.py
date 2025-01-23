import copy

def spread_fire(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    updated_grid = copy.deepcopy(grid)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                neighbors = []
                if i > 0:
                    neighbors.append(grid[i - 1][j])
                if i < rows - 1:
                    neighbors.append(grid[i + 1][j])
                if j > 0:
                    neighbors.append(grid[i][j - 1])
                if j < cols - 1:
                    neighbors.append(grid[i][j + 1])
                if 2 in neighbors:
                    updated_grid[i][j] = 2

    return updated_grid

