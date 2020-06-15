import pygame

WIDTH = 1000					#Largura da tela
HEIGHT = 650 					#Altura da Tela
FPS = 60		#Frames Per Second

#Imagens
background = 'background_png.png'
player = 'player.png'
handsanitizer = 'handsanitizer.png'
coronga = 'coronavirus.png'

#Dimensões dos objetos
player_WIDTH = 180			#Largura da imagem do jogador
palyer_HEIGHT = 80			#Altura da imagem do jogador
handsanitizer_WIDTH = 30 	#Largura da imagem do álcool gel
handsanitizer_HEIGHT = 40	#Altura da imagem do jogador
virus_WIDTH = 60
virus_HEIGHT = 48

#Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
brown = (165, 42, 42)

FONT_NAME = 'centurygothic'	#Fonte das escritas
TITLE = 'Corona Run'		#Título
HS_FILE = 'highscore.txt'	#Documento que armazena o highscore

gravity = 2              #Aceleração da gravidade
jump_size = 30           #Velocidade inicial do pulo
ground = HEIGHT*5//6     #Altura do chão

world_speed = -10	#Velocidade inicial do mundo

#Estados:
walking = 0
jumping = 1
falling = 2