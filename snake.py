import math, sys

from board_logic import *
from food_logic import *
from snake_logic import *

# SETUP
pygame.init()
pygame.display.set_caption('Snake by Dana')
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

snake = [(15, 15), (15, 16), (15, 17)]
direction = Direction.UP
food_pos = generate_food(snake)

def reset():
    global snake, direction, food_pos
    snake = [(15, 15), (15, 16), (15, 17)]
    direction = Direction.UP
    food_pos = generate_food(snake)

def quit():
    sys.exit()
    # TODO save scores

# GAMEPLAY LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            quit()
        
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

    try:
        draw_score(screen, len(snake))
        draw_food(screen, food_pos)

        food_collision = snake[0] == food_pos
        
        update_snake(snake, direction, food_collision)
        draw_snake(screen, snake)

        if food_collision:
            food_pos = generate_food(snake)
            REFRESH_MS = math.ceil(REFRESH_MS * SPEED_MULTIPLIER)
    except Exception:
        game_over_screen = True
        while game_over_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_SPACE: # play again
                        reset()
                        game_over_screen = False
                    
                    if event.key == pygame.K_q:
                        quit()

    pygame.display.update()
    pygame.time.wait(REFRESH_MS)
