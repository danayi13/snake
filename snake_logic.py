from board_logic import *

def draw_snake(screen, snake):
    if snake[0] in snake[1:]:
        game_over(screen)

    # draw head in different color
    head_row, head_col = snake[0]
    draw_piece(screen, head_row, head_col, HEAD_COLOR)

    for row, col in snake[1:]:
        draw_piece(screen, row, col, SNAKE_COLOR)


def update_snake(snake, direction, food_collision):
    if not food_collision:
        snake.pop()
    head_row, head_col = snake[0]

    if direction == Direction.UP:
        snake.insert(0, (head_row+Direction.UP.value[0], head_col+Direction.UP.value[1]))
    if direction == Direction.DOWN:
        snake.insert(0, (head_row+Direction.DOWN.value[0], head_col+Direction.DOWN.value[1]))
    if direction == Direction.LEFT:
        snake.insert(0, (head_row+Direction.LEFT.value[0], head_col+Direction.LEFT.value[1]))
    if direction == Direction.RIGHT:
        snake.insert(0, (head_row+Direction.RIGHT.value[0], head_col+Direction.RIGHT.value[1]))