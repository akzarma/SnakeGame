import random

import pygame

pygame.init()
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Snake Game')

my_snake_ords = []
oreo = []

x = 50
y = 50
step = 10
width = 10
snake_len = 10
height = 10
vel = 300

rand_x = random.randint(0, win_width)
rand_y = random.randint(0, win_height)
print(rand_x, rand_y)
old_oreo = True

head = 1  # 1 for right 2 for down and vice versa
run = True
while run:
    pygame.time.delay(vel)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if rand_x - 10 < x < rand_x + 10 and rand_y - 10 < y < rand_y + 10:
        rand_x = random.randint(0, win_width)
        rand_y = random.randint(0, win_height)
        snake_len += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= step
        head = -1
    if keys[pygame.K_RIGHT]:
        x += step
        head = 1
    if keys[pygame.K_UP]:
        y -= step
        head = -2
    if keys[pygame.K_DOWN]:
        y += step
        head = 2
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 255, 255), (rand_x, rand_y, width, height))
    if head == 1:
        x += step
    elif head == -1:
        x -= step
    elif head == 2:
        y += step
    elif head == -2:
        y -= step
    temp_x = x
    temp_y = y
    for i in range(snake_len):
        pygame.draw.rect(win, (255, 255, 255), (temp_x, temp_y, width, height))
        temp_x -= 11

    pygame.display.update()
pygame.quit()
