import pygame
from player import Player


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

SCALE = 1
GRAVITY = 0.75

FPS = 60
clock = pygame.time.Clock()

# window confing
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DUNGEON-CONQUEST')

GREY = (50, 50, 50)

player = Player(200, 200, SCALE)
moving_right = False 
moving_left = False

run = True

while run:

    print((player.image.get_width(),player.image.get_height()))

    screen.fill(GREY)
    pygame.draw.line(screen, (255, 0, 0), (0, 350), (SCREEN_WIDTH, 350))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player.rect.centerx, player.rect.centery, 100, 100))

    player.draw(screen)
    player.update_animation()
    player.move(moving_right, moving_left)
    player.jump(GRAVITY)

    pygame.display.flip()

    if moving_left or moving_right:
        player.is_runnig = True
    else:
        player.is_runnig = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_UP:
                player.is_jumping = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False

    clock.tick(FPS)

pygame.quit()
