import pygame
from animator import Animator, load_animation_images

class Enemy(Animator):
    
    def __init__(self, x, y):
        super().__init__('enemy')
        
        self.speed = 5
        self.health = 100
        self.time = 0
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.death_zone = pygame.Rect(self.rect.centerx, self.rect.centery, int(self.image.get_width() * 0.2), int(self.image.get_height() * 0.4))

        
        self.flip = True
        self.is_walking = True
        self.is_dead = False
        
        self.enemy_animation = {
            'Idel' : load_animation_images(self.sprite_name, 'Idel', scale=1.5),
            'Walk' : load_animation_images(self.sprite_name, 'Walk', scale=1.5),
            'Death': load_animation_images(self.sprite_name, 'Death', scale=1.5)
        }
    
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
    def update_animation(self):
        
        if self.is_dead == False:
            if self.is_walking:
                self.start_animation()
                self.animate(self.enemy_animation.get('Walk'))
            else:
                self.start_animation()
                self.animate(self.enemy_animation.get('Idel'))
        
        elif self.is_dead:
                self.start_animation()
                self.animate(self.enemy_animation.get('Death'))
                
                time = pygame.time.get_ticks()*0.001
                if self.enemy_animation.get('Death')[-1] == self.image and time > 2.5:
                    print(time)
                    self.kill()

        
    
    def take_damage(self, damage):
        self.health -= damage
        
        if self.health <= 0:
            self.is_walking = False
            self.is_dead = True            
                
    
    def ai(self):
        pass