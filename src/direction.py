from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    @staticmethod
    def get_direction(index):
        directions = {
            0: Direction.LEFT,
            1: Direction.UP,
            2: Direction.RIGHT,
            3: Direction.DOWN
        }
        return directions[index]
