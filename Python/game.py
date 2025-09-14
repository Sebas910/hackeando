import pygame 
import random

pygame.init()

screen = pygame.display.set_mode((640,640))

running = True

x = 20
y = 10
block_size = 10

game_over = False
snake = [(x,y), (x - block_size, y), (x - 2*block_size,y)]
apple = (random.randrange(0,620, block_size), random.randrange(0,620,block_size))

direction = ''
clock = pygame.time.Clock()


while running:
    screen.fill((0,0,0)) # para que se limpie la pantalla y no queden restos del objeto en movimiento

    # Handle events and update direction/position first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

    if direction == 'UP':
        y -= block_size
    elif direction == 'DOWN':
        y += block_size
    elif direction == 'LEFT':
        x -= block_size
    elif direction == 'RIGHT':
        x += block_size

    # Insert new head after updating x,y
    new_head = (x, y)
    snake.insert(0, new_head)

    # Check apple collision; use 0..640 to align with grid
    if snake[0] == apple:
        apple = (random.randrange(0,640, block_size), random.randrange(0,640,block_size))
        # do not pop: snake grows
    else:
        snake.pop()

    if not game_over:
        for segment in snake:
            pygame.draw.rect(screen, (0,255,0), (segment[0], segment[1], block_size, block_size))
        # draw apple once
        pygame.draw.rect(screen, (255,0,0),(apple[0],apple[1],block_size,block_size))   
    
    if x < 0 or x>= 640 or y < 0 or y>= 640:
        game_over = True
           
    if game_over:
        
        font = pygame.font.SysFont(None,72)
        text = font.render("FAILED", True, (255,0,0))
        screen.blit(text, (150,150))
    
    pygame.display.flip()  

   
    
    

    clock.tick(20) #fps a los que ira el juego
pygame.quit()