"""
Projeto Final Desoft - Pygame
Autores: Esther Dagir e Pedro Tibério
"""

from os import path
import sys #dps eu vou usar o sys.exit() pra acabar o jogo
import pygame
import random
from config import *
from sprites import *

class Game:
    def __init__(self):
        # Initialize game window, etc
        pygame.init() #Inicia pygame
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))	#Definição do tamanho da tela
        pygame.display.set_caption('Corona Run - Esther Dagir e Pedro Tiberio')	#Nome do jogo
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.load_data()
        self.background_rect = self.screen.get_rect()
        self.highscore = 0

        self.running = True

    def new(self):
        # Start a new game after game over
        self.score = 0
        
        self.all_sprites = pygame.sprite.Group()
        self.all_handsanitizers = pygame.sprite.Group()
        self.all_corona = pygame.sprite.Group()
        self.all_handsanitizers.add(self.handsanitizer)
        self.all_corona.add(self.corona)

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.handsanitizer)
        self.all_sprites.add(self.corona)

        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop update

        self.background_rect.x += world_speed
        if self.background_rect.right < 0:
            self.background_rect.x += self.background_rect.width
        if self.background_rect.left >= WIDTH:
            self.background_rect.x -= self.background_rect.width
        self.background_rect2 = self.background_rect.copy()
        self.background_rect2.x += self.background_rect2.width
        self.screen.blit(self.background, self.background_rect2)

        self.all_sprites.update()
        
        if self.corona.rect.right < 0:
            self.score += 10

        for sprite in self.all_sprites:
            if sprite.rect.right < 0:
                sprite.rect.x = random.randrange(800, 1000)

        #Die
        hits_pc = pygame.sprite.spritecollide(self.player, self.all_corona, True, pygame.sprite.collide_mask) #Se o player e o alcool colidirem o álcool some
        hits_ph = pygame.sprite.spritecollide(self.player, self.all_handsanitizers, True, pygame.sprite.collide_mask)
        if hits_pc:
            self.playing = False
            self.all_corona.add(self.corona)
            self.all_sprites.add(self.corona)
            self.corona.rect.x = random.randrange(800, 1200)

        if hits_ph:
            self.score += 10
            self.all_handsanitizers.add(self.handsanitizer)
            self.all_sprites.add(self.handsanitizer)
            self.handsanitizer.rect.x = random.randrange(800, 1200)
        
        if self.score > self.highscore:
            self.highscore = self.score

    def events(self):
        # Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game loop draw
        self.screen.blit(self.background, self.background_rect)        
        #self.screen.blit(titulo, (WIDTH/3.5, HEIGHT/4))

        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 28, brown, WIDTH/2, 15)

        pygame.display.update()
        pygame.display.flip()

    def draw_text(self ,text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.start_screen()
while g.running:
    g.new()
    g.gameover_screen()

pygame.quit()