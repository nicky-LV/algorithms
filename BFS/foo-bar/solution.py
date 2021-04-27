from collections import deque


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
    checked_coordinates = []

    # Queue is initialized with starting coordinate
    queue = deque([(0, 0)])

    while queue:
        y, x = queue[0]
        checked_coordinates.append((y, x))

        neighbors = find_neighbors(grid=grid, coordinates=(y, x))
        neighbor_list = []

        for neighbor in neighbors:
            # Coordinates of neighbor
            y2, x2 = neighbor
            # Checks if neighbor is wall
            if grid[y2][x2] == 1:
                pass

            else:
                if neighbor not in checked_coordinates:
                    neighbor_list.append(neighbor)
                    queue.append(neighbor)
                    checked_coordinates.append(neighbor)

        graph[(y, x)] = neighbor_list
        queue.popleft()

        print(f"Coords: ({y}, {x}) | Next move: {neighbor_list}")

    return graph


def find_depth(graph, grid, y, x):
    depth = 1
    coordinate = (y, x)
    found = False

    # Checks if point is wall
    if is_wall(grid=grid, y=y, x=x):
        return None

    else:
        while not found and coordinate != (0, 0):
            for key in graph.keys():
                if coordinate in graph[key]:
                    if key == (0, 0):
                        found = True

                    else:
                        coordinate = key
                        depth += 1

    return depth


def is_wall(grid, y, x):
    if grid[y][x] == 1:
        return True

    else:
        return False


grid = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]
graph = bfs(grid)
print(find_neighbors(grid, (2, 2)))
print(find_depth(graph, grid, 3, 3))