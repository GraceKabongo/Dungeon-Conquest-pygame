import pygame
import os

class Animator(pygame.sprite.Sprite):
    
    def __init__(self, sprite_name):
        super().__init__()
        self.sprite_name = sprite_name
        self.image = pygame.image.load(f'assets/{self.sprite_name}/Idel/0.png')
        self.current_frame = 0
        self.current_image = self.image
        self.animation = False


    def start_animation(self):
        self.animation = True
        

    def animate(self, animations, animation_speed=0.2):
        # get images by name and type of animation
        self.images = animations
        if self.animation:   
            self.current_frame += animation_speed
            if self.current_frame >= len(self.images):
                self.current_frame = 0
            
            self.image = self.images[int(self.current_frame)]
        

def load_animation_images(sprite_name : str, animation_type : str, scale=2):

    images = []
    path = f'assets/{sprite_name}/{animation_type}/'

    for num in range(len(os.listdir(path))):
        img_path = f'{path}/{num}.png'
        image = pygame.image.load(img_path).convert_alpha()
        images.append(pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale))))
        
    return images


