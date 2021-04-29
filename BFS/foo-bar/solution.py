import copy
from collections import deque


def solution(map):
    height = len(map) - 1
    width = len(map[0]) - 1

    graph, depth_graph = bfs(grid=map)

    # Shortest distance (breaking no walls)
    shortest_distance = find_depth(graph, map, height, width)
    if shortest_distance is False:
        shortest_distance = 10000

    # Counts number of walls
    wall_queue = deque()
    for row_id, row in enumerate(map):
        for col_id, col in enumerate(row):
            # Adds wall coordinate to wall_list
            if col == 1:
                wall_queue.append((row_id, col_id))

    # Breaks every wall and re-calculates shortest route.
    while wall_queue:
        grid_replica = copy.deepcopy(map)
        y, x = wall_queue[0]
        grid_replica[y][x] = 0

        graph_broken_wall, depth_graph_broken_wall = bfs(grid_replica)
        distance = find_depth(depth_graph=graph_broken_wall, grid=grid_replica, y=height, x=width)

        if distance:
            if distance < shortest_distance:
                shortest_distance = distance

        wall_queue.popleft()

    return shortest_distance


def find_neighbors(grid, coordinates):
    """
    :param grid:
    :param coordinates:
    :return neighbor_list: list - Coordinates of neighboring nodes.
    """
    y, x = coordinates

    neighbor_list = []
    width = len(grid[0]) - 1
    height = len(grid) - 1

    directions = {
        'up': (y - 1, x),
        'down': (y + 1, x),
        'left': (y, x - 1),
        'right': (y, x + 1)
    }

    neighbor_list = []

    if 0 < x < width:
        neighbor_list.append(directions['right'])
        neighbor_list.append(directions['left'])

    if 0 < y < height:
        neighbor_list.append(directions['up'])
        neighbor_list.append(directions['down'])

    if x == 0:
        neighbor_list.append(directions['right'])
    elif x == width:
        neighbor_list.append(directions['left'])
    if y == 0:
        neighbor_list.append(directions['down'])
    elif y == height:
        neighbor_list.append(directions['up'])

    return neighbor_list


def bfs(grid):
    graph = {}
    depth_graph = {}

    checked_coordinates = []

    height = len(grid) - 1
    width = len(grid[0]) - 1

    # Queue is initialized with starting coordinate
    queue = deque([(0, 0)])

    while queue:
        y, x = queue[0]

        if x == width and y == height:
            queue = None
            break

        else:
            checked_coordinates.append((y, x))
            neighbors = find_neighbors(grid=grid, coordinates=(y, x))
            # Non-wall neighbors (for traversing shortest distance)
            neighbor_list = []

            # All neighbors (for calculating depth)
            depth_list = []

            for neighbor in neighbors:
                # Coordinates of neighbor
                y2, x2 = neighbor
                # Checks if neighbor is wall
                if neighbor not in checked_coordinates:
                    depth_list.append(neighbor)

                    if grid[y2][x2] != 1:
                        neighbor_list.append(neighbor)
                        queue.append(neighbor)

                    checked_coordinates.append(neighbor)

            graph[(y, x)] = neighbor_list
            depth_graph[(y, x)] = depth_list
            queue.popleft()

    return graph, depth_graph


def find_depth(depth_graph, grid, y, x):
    """
    :rtype: int
    :param depth_graph: Nested List - Graph or depth graph.
    :param grid: Nested list - Initial Grid.
    :param y: int - Y index.
    :param x: int - X index
    :return: int - Depth
    """
    depth = 1
    coordinate = (y, x)
    found = False
    search = False

    # Initial search if the coordinate is in the graph (if not, it may not be solvable without breaking a wall)
    for key in depth_graph.keys():
        if coordinate in depth_graph[key]:
            search = True

    while not found and search:
        for key in depth_graph.keys():
            if coordinate in depth_graph[key]:
                if key == (0, 0):
                    found = True

                else:
                    coordinate = key
                depth += 1

    if search:
        return depth

    else:
        return False


def is_wall(grid, y, x):
    if grid[y][x] == 1:
        return True

    else:
        return False