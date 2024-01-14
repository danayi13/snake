import sys

from board_logic import *
from food_logic import *
from snake_logic import *

pygame.init()
pygame.display.set_caption('Snake by Dana')
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

snake = [(15, 15), (15, 16), (15, 17)]
direction = Direction.UP
food_pos = generate_food(snake)

# GAMEPLAY LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP and direction != Direction.DOWN:
                direction = Direction.UP
            
            if event.key == pygame.K_DOWN and direction != Direction.UP:
                direction = Direction.DOWN

            if event.key == pygame.K_LEFT and direction != Direction.RIGHT:
                direction = Direction.LEFT
            
            if event.key == pygame.K_RIGHT and direction != Direction.LEFT:
                direction = Direction.RIGHT

    screen.fill(BACKGROUND_COLOR)

    draw_food(screen, food_pos)

    food_collision = snake[0] == food_pos
    
    update_snake(snake, direction, food_collision)
    draw_snake(screen, snake)

    if food_collision:
        food_pos = generate_food(snake)
        REFRESH_MS -= INCREASE_SPEED

    pygame.display.update()
    pygame.time.wait(REFRESH_MS)