import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Hangman')

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP)*13)/2)
starty = 400
A = 65
for i in range(26):
	x = startx + GAP*2 + ((RADIUS*2 + GAP)*(i % 13))
	y = starty + ((i // 13)*(GAP + RADIUS*2))
	letters.append([x, y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#loading images
images = []
for i in range(7):
	image = pygame.image.load("hangman" + str(i) + ".png")
	images.append(image)


#color variables
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

#game variables
hangman_status = 0
words = ["VIRAT", "SACHIN", "DHONI", "DRAVID", "JADEJA", "BUMBRAH"]
word = random.choice(words)
guessed = []

clock = pygame.time.Clock()
run = True

def draw():
	win.fill(white)

	text = TITLE_FONT.render("HANGMAN by SpecTEviL", 1, black)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "

	text = WORD_FONT.render(display_word, 1, black)
	win.blit(text, (400, 200))

	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, black, (x,y), RADIUS, 3)
			text = LETTER_FONT.render(ltr, 1, black)
			win.blit(text, (x - text.get_width()/2, y - text.get_width()/2))

	win.blit(images[hangman_status], (150,100))
	pygame.display.update()

while run:
	clock.tick(60)

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			m_x, m_y = pygame.mouse.get_pos()
			for letter in letters:
				x, y, ltr, visible = letter
				if visible:
					dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
					if dis < RADIUS:
						letter[3] = False
						guessed.append(ltr)
						if ltr not in word:
							hangman_status += 1
	draw()
	won = True
	for letter in word:
		if letter not in guessed:
			won = False
			break
	if won:
		pygame.time.delay(1000)
		win.fill(white)
		text = WORD_FONT.render("YAY!!! You Won. You're a Champion", 1, green)
		win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
		pygame.display.update()
		pygame.time.delay(3000)
		break

	if hangman_status == 6:
		pygame.time.delay(1000)
		win.fill(white)
		text = WORD_FONT.render("Opps! You Lost! No Worries try again", 1, red)
		win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
		pygame.display.update()
		pygame.time.delay(3000)
		break

pygame.quit()