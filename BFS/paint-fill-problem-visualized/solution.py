"""
PYTHON 3.0+
"""

from collections import deque
from termcolor import colored


def solution(grid, x, y, value):
    """
    :param grid: list - Matrix of values.
    :param x: int - Horizontal coordinate index.
    :param y: int - Vertical coordinate index from the top of the matrix.
    :param value: int - Value to write.
    :return: str - Visual representation of the new grid and what was changed.
    """

    # Prints initial grid for illustration
    print(colored("===== Initial grid =====", 'red'))
    print_grid(grid=grid, value=value, starting=True)

    queue = deque([(y, x)])
    checked_points = []

    initial_value = grid[y][x]

    while queue:
        y, x = queue[0]
        point_value = grid[y][x]

        if (y, x) in checked_points:
            pass

        else:
            # Checks if point has the same value as the originally chosen coordinates.
            if point_value == initial_value:
                # Satisfies the condition. It's a neighbor with the same numerical value.
                neighbors = find_neighbors(grid=grid, x=x, y=y)
                # Adds neighbors to queue
                for neighbor in neighbors:
                    queue.append(neighbor)

                # Changes the value of point
                grid[y][x] = value

        # Pop coordinates off the queue
        queue.popleft()

        checked_points.append((y, x))

    # Illustrates new grid
    print(colored("===== Final grid =====", 'red'))
    print_grid(grid=grid, value=value)


def find_neighbors(grid, x, y):
    """

    :param grid: list - matrix of values.
    :param x: int - X coordinate.
    :param y: int - Y coordinate.
    :return: list - array of neighbors.
    """
    neighbors = []

    matrix_width = len(grid[0])
    matrix_height = len(grid)

    value = grid[y][x]

    if 0 < x < matrix_width - 1:
        # Adds right and left neighbors
        if valid_neighbor(grid=grid, x=x+1, y=y, value=value):
            neighbors.append((y, x + 1))

        if valid_neighbor(grid=grid, x=x-1, y=y, value=value):
            neighbors.append((y, x - 1))

    # Right edge case
    elif x == matrix_width - 1:
        # Adds left neighbor
        if valid_neighbor(grid=grid, x=x-1, y=y, value=value):
            neighbors.append((y, x-1))

    # Left edge case
    else:
        # Adds right neighbor
        if valid_neighbor(grid=grid, x=x+1, y=y, value=value):
            neighbors.append((y, x+1))

    if 0 < y < matrix_height - 1:
        # Adds above and below neighbors
        if valid_neighbor(grid=grid, x=x, y=y-1, value=value):
            neighbors.append((y-1, x))

        if valid_neighbor(grid=grid, x=x, y=y+1, value=value):
            neighbors.append((y+1, x))

    # Bottom edge case
    elif y == matrix_height - 1:
        # Adds above neighbor
        if valid_neighbor(grid=grid, x=x, y=y-1, value=value):
            neighbors.append((y-1, x))

    # Top edge case
    else:
        # Adds bottom neighbor
        if valid_neighbor(grid=grid, x=x, y=y+1, value=value):
            neighbors.append((y+1, x))

    return neighbors


def valid_neighbor(grid, x, y, value):
    value_of_coordinate = value
    if grid[y][x] == value_of_coordinate:
        return True

    else:
        return False


def print_grid(grid, value, starting=False):
    """
    :param grid: Array - The grid to print.
    :param starting: Boolean - Print the starting matrix.
    :return: str - Colored matrix
    """

    if starting:
        for row in grid:
            for point in row:
                print(colored(point, 'blue'), end=" ")

            print('')

    else:
        for row in grid:
            for point in row:
                if point == value:
                    print(colored(point, 'green'), end=" ")
                else:
                    print(colored(point, 'magenta'), end=" ")

            print('')


solution([
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 0]
], 1, 2, 5)