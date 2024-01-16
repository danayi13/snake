import pygame

from constants import *

def game_over(screen):
    font = pygame.font.SysFont('Comic Sans MS', 100)
    instruction_font = pygame.font.SysFont('Comic Sans MS', 33)
    text_surface = font.render('Game Over!', False, WHITE)
    intstruction_surface = instruction_font.render('Press (Space) to play again, (Q) to close', False, HEAD_COLOR)

    screen.fill(BACKGROUND_COLOR)
    screen.blit(text_surface, (BOARD_SIZE / 7, BOARD_SIZE / 3))
    screen.blit(intstruction_surface, (BOARD_SIZE / 9, BOARD_SIZE / 2))

    pygame.display.update()

    raise Exception("game over")

def draw_piece(screen, row: int, col: int, color: (int, int, int)):
    if row < 0 or row >= BOARD_UNITS or col < 0 or col >= BOARD_UNITS:
        game_over(screen)

    radius = UNIT_SIZE/2 - 1
    center = UNIT_SIZE * row + radius + 2, UNIT_SIZE * col + radius + 2
    pygame.draw.circle(screen, color, center, radius)

def draw_score(screen, score: int):
    font = pygame.font.SysFont('Comic Sans MS', 15)
    score_surface = font.render('Score: ' + str(score), False, GREY)
    screen.blit(score_surface, (10, 10))
