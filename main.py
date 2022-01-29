import pygame
from player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DUNGEON CONQUEST')

RED = (50, 50, 50)

player = Player()

run = True

while run:

    screen.fill(RED)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False


pygame.quit()
