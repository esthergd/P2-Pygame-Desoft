def load_assets():
	assets = {}
	assets['background'] = pygame.image.load('projeto_game/assets/img/background.png').convert()
	assets['player_img'] = pygame.image.load('projeto_game/assets/img/player.png').convert_alpha()
	assets['player_img'] = pygame.transform.scale(assets['player_img'], (player_WIDTH, palyer_HEIGHT))
	assets['handsanitizer_img'] = pygame.image.load('projeto_game/assets/img/handsanitizer.png').convert_alpha()
	assets['handsanitizer_img'] = pygame.transform.scale(assets['handsanitizer_img'], (handsanitizer_WIDTH, handsanitizer_HEIGHT))
	assets['corona_img'] = pygame.image.load('projeto_game/assets//img/cornavirus.png').convert_alpha()
	assets['corona_img'] = pygame.transform.scale(assets['corona_img'], (virus_WIDTH, virus_HEIGHT))
	return assets	