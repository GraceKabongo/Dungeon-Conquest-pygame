import pygame
from arrow import Arrow
from animator import Animator, load_animation_images

class Player(Animator):
    def __init__(self, x, y, scale):
        super().__init__('player')

        self.direction = 1
        self.velocity_y = 0
        self.velocity_x = 5
        
        self.flip = False
        self.is_runnig = False
        self.is_jumping = False
        self.in_air = False
        self.is_shooting = False
        self.current_animation_type = ''

        self.arrows = pygame.sprite.Group()

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # list of all player animation
        self.player_animations = {
            'Idel' : load_animation_images(self.sprite_name, 'Idel'),
            'Run'  : load_animation_images(self.sprite_name, 'Run'),
            'Jump' : load_animation_images(self.sprite_name, 'Jump'),
            'Attack' : load_animation_images(self.sprite_name, 'Attack')
        }

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    
    def move(self, moving_right, moving_left):
        dx = 0

        if moving_right:
            dx += self.velocity_x
            self.direction = 1
            self.flip = False
        elif moving_left:
            dx -= self.velocity_x
            self.direction = -1
            self.flip = True

        self.rect.x += dx
    
    def jump(self, GRAVITY):

        dy = 0

        if self.is_jumping == True and self.in_air == False:
            self.velocity_y = -11
            self.is_jumping = False
            self.in_air = True
        
        #apply gravity
        self.velocity_y += GRAVITY
        if self.velocity_y > 10:
            self.velocity_y
        
        dy += self.velocity_y

        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.y += dy


    def update_animation(self):
        if self.is_runnig:
            self.start_animation()
            self.animate(self.player_animations.get('Run'))
            self.current_animation_type = 'Run'
        elif self.in_air == True:
            self.start_animation()
            self.animate(self.player_animations.get('Jump'))
            self.current_animation_type = 'Jump'
        elif self.is_shooting:
            self.start_animation()
            self.animate(self.player_animations.get('Attack'), 0.2)
            self.current_animation_type = 'Attack'
        else:
            self.start_animation()
            self.animate(self.player_animations.get('Idel'))
            self.current_animation_type = 'Idel' 
        
        


    def shoot(self):
        if self.direction >=1:
            arrow = Arrow(self.rect.centerx + 120, self.rect.centery + 30, self.direction, scale=2) 
        else:
            arrow = Arrow(self.rect.centerx - 30, self.rect.centery + 30, self.direction, scale=2)   
        self.arrows.add(arrow)

        

        
