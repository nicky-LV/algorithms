from collections import deque


def solution(grid):
    """
    Returns the number of islands in the grid. BFS.
    :param grid: list - 2D binary grid. "1"s are land, "0"s are water.
    :return: int - the number of islands.
    """
    global checked_coordinates
    global island_count
    checked_coordinates = []
    island_count = 0

    for r_index, row in enumerate(grid):
        for c_index, value in enumerate(row):
            coordinate = (r_index, c_index)

            if value == "1" and coordinate not in checked_coordinates:
                find_islands(grid=grid, y=r_index, x=c_index)

    return island_count


def find_neighbors(grid, y, x):
    """
    Returns a list of the neighbors coordinates
    :param grid: list - 2D binary grid.
    :param y: int - y coordinate (0 inclusive).
    :param x: int -  x coordinate (0 inclusive).
    :return: list - list of neighbor coordinates
    """
    height = len(grid) - 1
    width = len(grid[0]) - 1

    directions = {
        'up': (y-1, x),
        'down': (y+1, x),
        'left': (y, x-1),
        'right': (y, x+1)
    }

    neighbors = []

    # x is not on the edge
    if 0 < x < width:
        # Add left & right neighbor
        neighbors.append(directions['left'])
        neighbors.append(directions['right'])

    # x is on the left edge
    elif x == 0:
        # Add right neighbor
        neighbors.append(directions['right'])

    # x is on the right edge
    elif x == width:
        # Add left neighbor
        neighbors.append(directions['left'])

    # same for y
    if 0 < y < height:
        # Add up & down neighbor
        neighbors.append(directions['up'])
        neighbors.append(directions['down'])

    # y is on the top edge
    elif y == 0:
        # Add down neighbor
        neighbors.append(directions['down'])

    # y is on the bottom edge
    elif y == height:
        # Add up neighbor
        neighbors.append(directions['up'])

    neighbors_parsed = []
    for neighbor in neighbors:
        if neighbor not in checked_coordinates:
            neighbors_parsed.append(neighbor)

    return neighbors_parsed


def find_islands(grid, y, x):
    global island_count
    is_land = lambda y_coord, x_coord: True if grid[y_coord][x_coord] == '1' else False

    queue = deque([(y, x)])
    while queue:
        _y, _x = queue[0]

        neighbors = find_neighbors(grid=grid, y=_y, x=_x)
        for neighbor in neighbors:

            if neighbor not in checked_coordinates:
                n_y, n_x = neighbor
                if is_land(n_y, n_x):
                    queue.append((n_y, n_x))

                else:
                    pass

                checked_coordinates.append(neighbor)

            else:
                pass

        # Once the points neighbors have been added, remove it from queue and mark it as "checked"
        checked_coordinates.append((_y, _x))
        queue.popleft()

    island_count += 1