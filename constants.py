from enum import Enum

REFRESH_MS = 200
INCREASE_SPEED = 10


# Board Info
UNIT_SIZE   = 25
BOARD_UNITS = 30
BOARD_SIZE  = UNIT_SIZE * BOARD_UNITS


# Colors
BACKGROUND_COLOR = 0, 0, 0
SNAKE_COLOR      = 153, 204, 255
HEAD_COLOR       = 51, 153, 255
FOOD_COLOR       = 255, 0, 0
WHITE            = 255, 255, 255


class Direction(Enum):
    UP    = (0, -1)
    DOWN  = (0, 1)
    LEFT  = (-1, 0)
    RIGHT = (1, 0)