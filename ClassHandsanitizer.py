class Handsanitizer(pygame.sprite.Sprite):
	def __init__(self, groups, assets):
		pygame.sprite.Sprite.__init__(self)
		self.image = assets['handsanitizer_img']
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(600, WIDTH + handsanitizer_WIDTH)
		self.rect.y = random.randint(30,600)
		self.rect.bottom = ground
		self.speedx = 0
		self.speedy = 0