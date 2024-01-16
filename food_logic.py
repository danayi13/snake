import random

from board_logic import *

def draw_food(screen, food_pos: (int, int)):
    draw_piece(screen, food_pos[0], food_pos[1], FOOD_COLOR)

def generate_food(snake: []):
    # TODO make more efficient
    while True:
        food_pos = (random.randint(0, 29), random.randint(0, 29))
        if food_pos not in snake:
            return food_pos