"""
Projeto Final Desoft - Corona Run
Autores: Esther Dagir e Pedro Tibério
"""

from os import path
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
        pygame.display.set_caption('Corona Run - Esther Dagir e Pedro Tibério')	#Nome do jogo
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.load_data()
        self.background_rect = self.screen.get_rect()
        self.highscore = 0
        self.world_speed = -10   #Velocidade inicial do mundo

        self.running = True

    def load_data(self):
        self.dir = path.dirname(__file__)
        #Imagens
        img_dir = path.join(self.dir, 'img')
        self.background = pygame.image.load(path.join(img_dir, 'background_png.png')).convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.player = Player()
        self.handsanitizer = Handsanitizer()
        self.corona = Corona()

        #Sons
        self.snd_dir = path.join(self.dir, 'sounds')
        self.go_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'GameOver.wav'))
        pygame.mixer.music.load(path.join(self.snd_dir, 'musicafundo.mp3'))

        #Dim screen para o pause
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0,0,0,180))

        #Dim screen para o game over
        self.dim_screen2 = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen2.fill((180,0,0,180))

        #Highscore
        with open(path.join(self.dir, HS_FILE), 'w') as hs:
        	try:
        		self.highscore = int(hs.read())
       		except:
        		self.highscore = 0


    def new(self):
        # Start a new game after game over
        pygame.mixer.music.unpause()
        self.score = 0
        self.estoque_alcool = 3
        self.world_speed = world_speed
        
        self.all_sprites = pygame.sprite.Group()
        self.all_handsanitizers = pygame.sprite.Group()
        self.all_corona = pygame.sprite.Group()
        self.all_handsanitizers.add(self.handsanitizer)
        self.all_corona.add(self.corona)

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.handsanitizer)
        self.all_sprites.add(self.corona)

        self.paused = False #Para a tela de pause

        self.run()

        

    def run(self):
        # Game loop
        self.playing = True
        pygame.time.set_timer(pygame.USEREVENT, 8000)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            if not self.paused:
            	self.update()
            self.draw()

    def update(self):
        # Game loop update

        self.background_rect.x += self.world_speed
        if self.background_rect.right < 0:
            self.background_rect.x += self.background_rect.width
        if self.background_rect.left >= WIDTH:
            self.background_rect.x -= self.background_rect.width

        self.all_sprites.update()
        
        if self.corona.rect.right < 0:
            self.score += 10

        if self.handsanitizer.rect.right < 0:
            self.estoque_alcool -= 1

        if self.estoque_alcool == 0:
            self.playing = False

        for sprite in self.all_sprites:
            if sprite.rect.right < 0:
                sprite.rect.x = random.randrange(1000, 1400)
            sprite.speedx = self.world_speed

        #Die
        hits_pc = pygame.sprite.spritecollide(self.player, self.all_corona, True, pygame.sprite.collide_mask)
        hits_ph = pygame.sprite.spritecollide(self.player, self.all_handsanitizers, True, pygame.sprite.collide_mask)
        if hits_pc:
            self.playing = False
            self.go_sound.play()
            self.go_sound.set_volume(.5)
            self.all_corona.add(self.corona)
            self.all_sprites.add(self.corona)
            self.corona.rect.x = random.randrange(1000, 1400)

        if hits_ph:
            self.score += 10
            self.all_handsanitizers.add(self.handsanitizer)
            self.all_sprites.add(self.handsanitizer)
            self.handsanitizer.rect.x = random.randrange(1000, 1400)
            self.estoque_alcool += 1

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

                if event.key == pygame.K_p:
                    self.paused = not self.paused

            if event.type == pygame.USEREVENT:
        	    self.world_speed -= 1

    def draw(self):
        # Game loop draw
        self.screen.blit(self.background, self.background_rect)
        self.background_rect2 = self.background_rect.copy()
        self.background_rect2.x += self.background_rect2.width
        self.screen.blit(self.background, self.background_rect2)

        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 28, brown, WIDTH/2, 15)
        self.draw_text('Alcohol in stock: ' + str(self.estoque_alcool), 24, brown, 125, 18)

        if self.paused:
        	self.screen.blit(self.dim_screen, (0,0))
        	self.draw_text("PAUSED", 30, brown, WIDTH/2, HEIGHT/2)

        pygame.display.update()
        pygame.display.flip()

    def draw_text(self ,text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def start_screen(self):
        pygame.mixer.music.play(loops = -1)
        pygame.mixer.music.set_volume(.1)
        self.screen.blit(self.background, self.background_rect)
        self.draw_text(TITLE, 50, brown, WIDTH/2, HEIGHT/5)
        self.draw_text("Use space key to jump and P to pause", 24, brown, WIDTH/2, HEIGHT/2.5)
        self.draw_text("Press any key to start", 24, brown, WIDTH/2, HEIGHT/1.75)
        self.draw_text("Highscore: " + str(self.highscore), 24, brown, WIDTH/2, 30)
        pygame.display.flip()
        self.wait_for_key()

    def gameover_screen(self):
        # Tela de game over
        if self.running == False:
            return
        pygame.mixer.music.pause()
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.dim_screen2, (0,0))
        self.draw_text("You caught corona...", 50, white, WIDTH/2, HEIGHT/6)
        self.draw_text("Score: " + str(self.score), 24, white, WIDTH/2, HEIGHT/3)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!" , 28, white, WIDTH/2, HEIGHT/2-40)
            with open(path.join(self.dir, HS_FILE), 'w') as hs:
                hs.write(str(self.score))
        else:
            self.draw_text("Highscore: " + str(self.highscore), 24, white, WIDTH/2, HEIGHT/2-40)

        self.draw_text("Alcohol in stock: " + str(self.estoque_alcool), 24, white, WIDTH/2, HEIGHT/2+25)
        self.draw_text("Press any key to play again", 24, white, WIDTH/2, HEIGHT*2/3)
        
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        wait = True
        while wait:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    wait = False

g = Game()
g.start_screen()
while g.running:
    g.new()
    g.gameover_screen()

pygame.quit()