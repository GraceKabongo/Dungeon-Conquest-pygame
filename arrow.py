import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, scale):
        super().__init__()
        
        self.speed = 10
        self.image = pygame.image.load('assets/arrow.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.flip = False 

    def move(self):
        if self.direction == -1:
            self.flip = True
        else:
            self.flip = False       
        
        self.rect.x += self.speed * self.direction
        
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
	    
    

