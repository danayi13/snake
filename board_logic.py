import pygame

from constants import *

def game_over(screen):
    font = pygame.font.SysFont('Comic Sans MS', 100)
    text_surface = font.render('Game Over!', False, WHITE)

    screen.fill(BACKGROUND_COLOR)
    screen.blit(text_surface, (BOARD_SIZE / 7, BOARD_SIZE / 3))


def draw_piece(screen, row, col, color):
    if row < 0 or row >= BOARD_UNITS or col < 0 or col >= BOARD_UNITS:
        game_over(screen)
        return # TODO make it exit right away

    radius = UNIT_SIZE/2 - 1
    center = UNIT_SIZE * row + radius + 2, UNIT_SIZE * col + radius + 2
    pygame.draw.circle(screen, color, center, radius)
