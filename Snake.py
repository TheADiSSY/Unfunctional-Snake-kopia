#SNAKE?! SNAAAAAAAAAAAAAKEEEEEE!!!

import pygame
import random
import time

pygame.display.set_caption("Snake")


direction_x = 0
direction_y = 0

beige = (174, 165, 141)
red = (255, 0, 0)

#This will initiate the game
pygame.init()
screen = pygame.display.set_mode((1200, 500))
clock = pygame.time.Clock()
running = True
dt=0.005

snake_x= 600
snake_y= 250
snake_size = 30

food_x = random.randint(1,119) * (10)
food_y = random.randint(1,49) * (10)
Snake_body = []

score = 0

#For closing the game down. "pygame.QUIT" lets the app recognise when X is pressed on the window, closing the program.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#This will let us put everything in our screen
    pygame.display.flip()


#This will set the framerate of the game
    clock.tick(30)


#Background colour. This, for instance, is hexcode for a type of brown
    screen.fill("#685b38")


#The snake itself. it will be placed in "screen", the first parentheses is the snake's rgb value, the second parentheses is its coordinates and size measurement in that order.
    snake_head = pygame.draw.rect(screen, (174, 165, 141), (snake_x,snake_y, 30, 30))
    length = 1

#These are the border rules
    
    if snake_x >= 1200: 
        running = False
    elif snake_y >= 500:
        running = False
    elif snake_x <= 0:
        running = False
    elif snake_y <= 0:
        running = False
    
    #Snake length, food and score distribution

    Food_spawn = True

    if snake_x == food_x and snake_y == food_y:
        score = score + 1
        snake_size = snake_size + 1
        Food_spawn = False
    if Food_spawn == False:
        food_x = random.randint(1,119) * (10)
        food_y = random.randint(1,49) * (10)
        Snake_body.append(pygame.Rect(snake_x, snake_y, snake_size, snake_size)) 
        time.sleep(1/30)
    if len(Snake_body) > snake_size:
        del Snake_body[0]
    if Food_spawn == True:
        pygame.draw.rect(screen, (255,0,0), (food_x, food_y, 30,30))




#Player controls

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction_y = -10
        direction_x=0
    if keys[pygame.K_s]:
        direction_y = +10
        direction_x=0
    if keys[pygame.K_a]:
        direction_x = -10
        direction_y=0
    if keys[pygame.K_d]:
        direction_x = +10
        direction_y=0

    snake_x = snake_x + direction_x
    snake_y = snake_y + direction_y



print("Your score was", score, "!")