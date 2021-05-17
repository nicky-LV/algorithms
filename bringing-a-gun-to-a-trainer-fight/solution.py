import itertools
from collections import deque


def solution(dimensions, your_position, trainer_position, distance):
    my_coord_x, my_coord_y = your_position

    points = []
    queue = deque([trainer_position])
    while queue:
        pos_vector_to_reflect = queue[0]
        reflected_points = reflect_pos_vector(pos_vector_to_reflect, dimensions)

        for point in reflected_points:
            if isWithinRadius(your_position, point, distance) and point not in points:

                # We have to remove any points that have the same y coordinate as our position (and are to our left, so x < 0).
                # Otherwise the beam would reflect and hit us
                if point[1] == my_coord_y and point[0] < my_coord_x:
                    pass

                else:
                    points.append(point)
                    queue.append(point)

        queue.popleft()

    direction_vectors = find_direction_vectors(your_position, points)
    # todo: remove direction vectors which are scalar multiples of eachother
    return direction_vectors


def isWithinRadius(your_position, position_vector, distance):
    """
    Checks whether a coordinate is within the specified distance from a point (so the beam can reach it).
    :param your_position: tuple of your starting (x, y) coordinates
    :param distance: int - the distance the beam can travel
    :return: boolean - True/False depending on if the coordinate can be reached by the beam.
    """
    my_coord_x, my_coord_y = your_position
    position_v_x, position_v_y = position_vector

    change_y, change_x = abs(position_v_y - my_coord_y), abs(position_v_x - my_coord_x)
    # Euclidean distance between points
    dist = ((change_x ** 2) + (change_y ** 2))**0.5

    if dist < distance:
        return True

    else:
        return False

def findCorners(dimensions):
    x, y = dimensions
    # Bottom left corner has coordinates (0, 0)
    corners = [(0, 0), (x, 0), (x, y), (0, y)]
    return corners

def reflect_pos_vector(position_vector, dimensions):
    x, y = dimensions
    pos_x, pos_y = position_vector
    reflected_points = []
    # Reflect by top wall
    y_change = y - pos_y
    reflected_points.append((pos_x, pos_y + 2*(y_change)))

    # Reflect by bottom wall
    y_change = 0 - pos_y
    reflected_points.append((pos_x, pos_y + 2*(y_change)))

    # Reflect by right wall
    x_change = x - pos_x
    reflected_points.append((pos_x + 2*x_change, pos_y))

    # Reflect by left wall
    x_change = 0 - pos_x
    reflected_points.append((pos_x + 2*x_change, pos_y))

    return reflected_points


def find_direction_vectors(your_position, position_vectors):
    direction_vectors = []
    x, y = your_position
    for position in position_vectors:
        pos_x, pos_y = position
        direction_x = pos_x - x
        direction_y = pos_y - y
        direction_vector = (direction_x, direction_y)
        direction_vectors.append(direction_vector)

    return direction_vectors


def parse_direction_vectors(direction_vectors):
    """ Removes direction vectors which are scalar multiples of eachother. """
    parsed_direction_vectors = []
    multiplier_x = 0
    y_multiplier_y = 0
    for d_vector in direction_vectors:
        d_x, d_y = d_vector
        for other_vector in direction_vectors:
            o_x, o_y = other_vector

            try:
                multiplier_x = d_x / o_x
            except ZeroDivisionError:
                pass

            try:
                multiplier_y = d_y / o_y
            except ZeroDivisionError:
                pass

        if multiplier_x is not 0 and multiplier_y is not 0 and

print(solution([3,2], [1,1], [2,1], 4))

