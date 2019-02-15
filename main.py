import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Spaghetti User Interface")

screenWidth = 500
screenHeight = 500

clock = pygame.time.Clock()

#spawn position
x = 250 
y = 250

#sprite dimensions
width = 40 
height = 60

vel = 5

run = True
isJump = False
jumpCount = 10

#main game loop
while run:
	clock.tick(60) #60 fps
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
	if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
		x += vel
	if not(isJump):
		#platform game - disabling upwards and downwards movement
		'''if keys[pygame.K_UP] and y > vel:
			y -= vel
		if keys[pygame.K_DOWN] and y < screenHeight - height - vel:				    y += vel'''
		#enabling jumping
		if keys[pygame.K_SPACE]:
			isJump = True
	else: #jumping
		if jumpCount >= -10: #parabolic jump
			y -= (jumpCount * abs(jumpCount)) * 0.5 
			jumpCount -= 1
		else: #end of jump
			isJump = False
			jumpCount = 10

	win.fill((0, 0, 0))
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()

pygame.quit()	
 
