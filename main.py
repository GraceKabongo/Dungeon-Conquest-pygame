import pygame
from enemy import Enemy
from player import Player


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

SCALE = 2
GRAVITY = 0.75
COUNTER_SHOT = 0

FPS = 60
clock = pygame.time.Clock()

# window confing
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DUNGEON-CONQUEST')

background_image = pygame.image.load('assets/Background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(200, 200)
enemy_group = pygame.sprite.Group()
enemy_group.add(Enemy(400, 250))

moving_right = False 
moving_left = False

run = True

while run:

    screen.blit(background_image, (0, 0))
    pygame.draw.line(screen, (0, 0, 200), (0, 350), (SCREEN_WIDTH, 350))

        
    for enemy in enemy_group:
            
        enemy.draw(screen)
        enemy.update_animation()
        
        # TODO : FIX THIS BUG
        
        for arrow in player.arrows:
            arrow.draw(screen)
            arrow.move()
        
            if arrow.rect.colliderect(enemy.death_zone):
                arrow.kill()
                enemy.take_damage(50)
                print(f'enemy health = {enemy.health}')

    player.draw(screen)
    player.update_animation()
    player.move(moving_right, moving_left)
    player.jump(GRAVITY)

    pygame.display.flip()

    if moving_left or moving_right:
        player.is_runnig = True
    else:
        player.is_runnig = False
    
    if player.is_shooting == True:
        if player.player_animations.get('Attack')[-2] == player.image:
            player.shoot()
            player.is_shooting = False
        player.start_animation()


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
            elif event.key == pygame.K_SPACE:
                
                player.is_shooting = True
        
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False

    clock.tick(FPS)

pygame.quit()
