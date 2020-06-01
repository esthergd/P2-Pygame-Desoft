class Player(pygame.sprite.Sprite):
	def __init__(self, groups, assets):
		pygame.sprite.Sprite.__init__(self)

		self.image = assets['player_img']
		self.mask = pygame.mask.from_surface(self.image)
		self.state = walking
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.top = 0 #pra que que é esse rect.top?
		self.rect.x = 0
		self.rect.y = 0
		self.speedy = 0
		self.velocidade_player = 0.3  #mesma coisa que self.speedx
		self.pos_player = [0,0]
		self.delta_player = {'direita': 0, 'esquerda': 0}
		
	def update(self):
		self.speedy += gravity
		if self.speedy > 0:
			self.state = falling
			self.rect.y += self.speedy

		if self.rect.bottom > ground:
			self.rect.bottom = ground
			self.speedy = 0
			self.state = walking

		self.rect.x += self.velocidade_player
		if self.rect.x > pygame.display.get_surface().get_width() - self.rect.width:
			self.velocidade_player = -self.velocidade_player
			self.rect.x = pygame.display.get_surface().get_width() - self.rect.width
		elif self.rect.x < 0:
			self.velocidade_player = -self.velocidade_player
			self.rect.x = 0

	def jump(self):
		if self.state == walking:
			self.speedy = jump_size
			self.state = jumping