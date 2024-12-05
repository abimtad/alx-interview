#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid representing the island and water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check above
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                # Check below
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                # Check left
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                # Check right
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter
