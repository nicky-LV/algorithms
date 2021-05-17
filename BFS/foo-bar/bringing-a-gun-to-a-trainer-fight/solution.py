def solution(dimensions, your_position, trainer_position, distance):
    pass


def hit_corner(bearing):
    """
    Returns bearing in the opposite direction
    :param bearing: list - [x, y] bearing.
    :return: list [x, y] bearing in the opposite direction.
    """
    x, y = bearing
    return [-x, -y]


"""
0 0 0 0
0 X Y 0
0 0 0 0
"""