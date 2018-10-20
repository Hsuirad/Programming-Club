import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

a = -400 
j = -200

gDisp = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Racing Game")

clock = pygame.time.Clock()

#height = 214px, width = 160px
carImage = pygame.image.load('/home/daligholi/Desktop/Untitled.png')
backg = pygame.image.load('/home/daligholi/Desktop/background.png')
enemy = pygame.image.load('/home/daligholi/Desktop/bntitled.png')

def things_dodge(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " + str(count), True, white)
	gDisp.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
	#pygame.draw.rect(gDisp, color, [thingx, thingy, thingw, thingh])
	gDisp.blit(enemy, (thingx, thingy))

def car(x, y):
	gDisp.blit(carImage, (x, y))

def text_objects(text, font):
	text_surface = font.render(text, True, black)
	return text_surface, text_surface.get_rect()

def message_display(text):
	large_text = pygame.font.Font("freesansbold.ttf", 108)
	TextSurf, TextRect = text_objects(text, large_text)
	TextRect.center = ((display_width / 2), (display_height / 2))
	gDisp.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def check_crash(dodged):
	message_display("You Scored " + str(dodged) + "!")

def back(x, y):
	gDisp.blit(backg, (0, 0))


def game_loop():

	x = (display_width * 0.2)
	y = (display_height * 0.5)

	car_width = 112
	car_height = 140
	enemy_width = 84
	enemy_height = 106

	x_change = 0
	y_change = 0

	things_startx = random.randrange(0, (display_width - 100))
	thing_starty = -600
	things_speed = 3
	things_width = 100
	things_height = 100

	dodged = 0

	game_exit = False

	while game_exit == False:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = (things_speed * -0.8)
				elif event.key == pygame.K_RIGHT:
					x_change = (things_speed * 0.8)
				elif event.key == pygame.K_UP:
					y_change = (things_speed * -0.8)
				elif event.key == pygame.K_DOWN:
					y_change = (things_speed * 0.8)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0


		x += x_change
		y += y_change

		gDisp.fill(white)

		back(0, 0)
		things(things_startx, thing_starty, things_width, things_height, red)
		thing_starty += things_speed
		car(x, y)
		things_dodge(dodged)

		if (x > (display_width - car_width) or x < 0) or (y > (display_height - car_height) or y < 0):
			check_crash(dodged)

		if x > (things_startx) and x < (things_startx + enemy_height) and y < (thing_starty + enemy_height) and y > thing_starty:
			check_crash(dodged)
		if (x + car_width) < (things_startx + enemy_width) and (x + car_width) > things_startx and y > thing_starty and y < (thing_starty + enemy_height):
			check_crash(dodged)

		if thing_starty > display_height:
			thing_starty = 0 - things_height
			things_startx = random.randrange(0, (display_width - 100))
			dodged += 1
			things_speed += 1
		print(x, y)
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()
