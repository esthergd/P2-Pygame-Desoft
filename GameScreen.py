def game_screen(window):
	clock = pygame.time.Clock()
	assets = load_assets()

	background = assets['background']
	background_rect = background.get_rect()

	all_sprites = pygame.sprite.Group()
	all_handsanitizers = pygame.sprite.Group()
	all_coronavirus = pygame.sprite.Group()
	groups = {}
	groups['all_sprites'] = all_sprites
	groups['all_handsanitizers'] = all_handsanitizers
	groups['all_coronavirus'] = all_coronavirus

	player = Player(groups, assets)
	handsanitizer = Handsanitizer(groups, assets)
	corona = Corona(groups, assets)
	all_sprites.add(player, handsanitizer, corona)

	#for i in range (INITIAL_BLOCKS):
	#	block_x = random.randint(0, WIDTH)
	#	block_y =  

	#Outros estados:
	playing = 0
	done = 1
	state = playing

	while state != done:
		delta_time = clock.tick(FPS)
		#Eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				state = done

			if state == playing:
				if event.type == pygame.KEYDOWN:
					#keys_down[event.key] = True
					if event.key == pygame.K_SPACE:
						player.jump()

					if event.key == pygame.K_RIGHT:
						player.delta_player['direita'] = 1
					elif event.key == pygame.K_LEFT:
						player.delta_player['esquerda'] = 1

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						player.delta_player['direita'] = 0
					if event.key == pygame.K_LEFT:
						player.delta_player['esquerda'] = 0

		if state == playing:
			hits = pygame.sprite.spritecollide(player, all_handsanitizers, False, True) #Se o player e o alcool colidirem o álcool some


		pos_player = player.delta_player['direita'] - player.delta_player['esquerda'] * player.velocidade_player * delta_time

		all_sprites.update()
		all_sprites.draw(window)

		background_rect.x += world_speed
		if background_rect.right < 0:
            background_rect.x += background_rect.width

		# ----- Gera saídas
		window.fill(black)
		window.blit(background, background_rect)
		window.blit(frasecapa, (150, 200))
		window.blit(corona.image, (300, 560))
		window.blit(player.image, (100, ground))
		window.blit(handsanitizer.image, (200, ground))

		background_rect2 = background_rect.copy()
		background_rect2.x += background_rect2.width
		screen.blit(background, background_rect2)

		pygame.display.update()