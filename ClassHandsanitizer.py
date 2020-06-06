class Handsanitizer(pygame.sprite.Sprite):
	def __init__(self, groups, assets):
		pygame.sprite.Sprite.__init__(self)
		self.image = assets['handsanitizer_img']
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(300, 600)
		self.rect.y = ground
		self.rect.bottom = ground
		self.speedx = world_speed

	def update(self):
		self.rect.x += self.speedx 