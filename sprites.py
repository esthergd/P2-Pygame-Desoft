from os import path
import pygame
import random 
from config import *

dir = path.dirname(__file__)
img_dir = path.join(dir, 'img')

class Player(pygame.sprite.Sprite):
    def __init__(self): #add game se precisar
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(img_dir, 'player.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (player_WIDTH, palyer_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.state = walking
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2 - 100
        self.rect.bottom = ground
        self.speedy = 0
        self.dir = path.dirname(__file__)
        self.snd_dir = path.join(self.dir, 'sounds')
        self.jump_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'jump_07.wav'))
        self.jump_sound.set_volume(.2)

    def update(self):
        self.speedy += gravity
        if self.speedy > 0:
            self.state = falling
        self.rect.y += self.speedy

        if self.rect.bottom > ground:
            self.rect.bottom = ground
            self.speedy = 0
            self.state = walking

    def jump(self):
        if self.state == walking:
            self.speedy -= jump_size
            self.state = jumping
            self.jump_sound.play()

class Handsanitizer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir, 'handsanitizer.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (handsanitizer_WIDTH, handsanitizer_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1000, 1400)
        self.rect.bottom = ground - 200
        self.speedx = world_speed

    def update(self):
        self.rect.x += self.speedx

class Corona(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load(path.join(img_dir, 'coronavirus.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (virus_WIDTH, virus_HEIGHT))
        self.image.set_colorkey(white)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1000, 1400)
        self.rect.bottom = ground-10
        self.speedx = world_speed
    
    def update(self):
        self.rect.x += self.speedx