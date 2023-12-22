import sys
from utils import *

pygame.init()
pygame.display.set_caption('Snake by Dana')
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

snake = [(10, 10)]
direction = Direction.UP

# GAMEPLAY LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP:
                direction = Direction.UP
            
            if event.key == pygame.K_DOWN:
                direction = Direction.DOWN

            if event.key == pygame.K_LEFT:
                direction = Direction.LEFT
            
            if event.key == pygame.K_RIGHT:
                direction = Direction.RIGHT

    screen.fill(BACKGROUND_COLOR)
    
    update_snake(snake, direction)
    draw_snake(screen, snake)

    pygame.display.flip()
    pygame.time.wait(REFRESH_MS)