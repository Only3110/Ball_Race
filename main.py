#Gundu Race program
import turtle
import time
import random

WIDHT, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'brown', 'violet', 'pink', 'black']

def get_number_of_racer():
	racers = 0
	while True:
		racers = input('Enter the number of racers(2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Invalid input, try again in numeric!')
			continue
		if 2 <= racers <= 10:
			return racers
		else:
			print('Invalid input, try again in range 2 - 10!')

def gas(colors):
	gundu = create_gundu(colors)

	while True:
		for racer in gundu:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[gundu.index(racer)]

def create_gundu(colors):
	gundu = []
	spacingx = WIDHT // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('circle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDHT //2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		gundu.append(racer)
	
	return gundu

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDHT, HEIGHT)
	screen.title('Ball Race')

racers = get_number_of_racer()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = gas(colors)
print("The winner is", winner)