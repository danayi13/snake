from constants import *
import pygame

def game_over(screen):
    font = pygame.font.SysFont('Comic Sans MS', 100)
    text_surface = font.render('Game Over!', False, WHITE)

    screen.fill(BACKGROUND_COLOR)
    screen.blit(text_surface, (BOARD_SIZE / 7, BOARD_SIZE / 3))

    return


def draw_snake_piece(screen, row, col):
    if row < 0 or row >= BOARD_UNITS or col < 0 or col >= BOARD_UNITS:
        game_over(screen)
        return

    radius = UNIT_SIZE/2 - 1
    center = UNIT_SIZE * row + radius + 2, UNIT_SIZE * col + radius + 2
    pygame.draw.circle(screen, SNAKE_COLOR, center, radius)


def draw_snake(screen, snake):
    for row, col in snake:
        draw_snake_piece(screen, row, col)


def update_snake(snake, direction):
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