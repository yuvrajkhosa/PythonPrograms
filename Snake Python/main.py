import math, sys, pygame
from random import randint
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
amountToAdd = 50
gridSize = 10
clock = pygame.time.Clock() # Used to set FPS
class Snake:
	def __init__(this): #Constructor
		this.pos = [[50, 50]] #Position Vector
		this.xAdd = 1 # Whether to add 1 or -1 in the x axis
		this.yAdd = 0 # Whether to add 1 or -1 in the y axis
		this.snakeSize = 1
	def show(this):
		for i in range(this.snakeSize):
			pygame.draw.rect(screen, (255, 0, 0), (this.pos[i][0], this.pos[i][1], gridSize, gridSize))

		tempPos = this.pos[0][:] #This is the actaul VALUE and the not the reference to the this.pos variable. Makes a copy
		this.pos[0][0] += gridSize * this.xAdd #Add to the x coordinate if xAdd is not 0. It can be 1 or -1.
		this.pos[0][1] += gridSize * this.yAdd #Add to the y coordinate if yAdd is not 0. It can be 1 or -1.
		if(this.snakeSize > 1): #IF the snake has a tail. SHift all the elements in the histroy down
			for i in range(this.snakeSize - 1, 1, -1): #Go from last index to up to NOT INCLUDING second. Make last index to second last and so on
				this.pos[i] = this.pos[i - 1] #Change them. Go down by one
			this.pos[1] = tempPos #Set the second one to the head. The head gets a brand new one


	def checkCollision(this):
		for i in range(1, this.snakeSize):
			if(this.pos[i] == this.pos[0]):
				print("DEAD")
		if(this.pos[0][0] > width or this.pos[0][0] < 0 or this.pos[0][1] > height or this.pos[0][1] < 0):
			print("Dead")

	def move(this, x , y):
		this.xAdd = x #Set xAdd to 1, -1, or 0
		this.yAdd = y #Set yAdd to 1, -1, or 0
	def checkFood(this, food):
		if(this.pos[0][0] == food.pos[0] and this.pos[0][1] == food.pos[1]): #If snake is touching the food
			food.newLocation()
			for i in range(amountToAdd): #This makes sure that we are adding a new position for the element right above.
				this.pos.append([this.pos[i][0], this.pos[i][1]]) # Each new element gets the spot above it
			this.snakeSize += amountToAdd

class Food:
	def __init__(this):
		this.pos = [0, 0] # Get random positin and round it to nearest TEN
		this.newLocation()
	def show(this):
		pygame.draw.rect(screen, (255, 255, 0), (this.pos[0], this.pos[1], gridSize, gridSize))
	def newLocation(this):
		this.pos = [math.ceil(randint(0, width - gridSize) / 10.0) * 10, math.ceil(randint(0, height - gridSize) / 10.0) * 10] # Get random positin and round it to nearest TEN
snake = Snake()
food = Food()


while True:
	for event in pygame.event.get(): #Close game if 'X' Clicked

		if(event.type == pygame.QUIT): sys.exit()

		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_DOWN):
				snake.move(0, 1)
			if(event.key == pygame.K_UP):
				snake.move(0, -1)
			if(event.key == pygame.K_RIGHT):
				snake.move(1, 0)
			if(event.key == pygame.K_LEFT):
				snake.move(-1, 0)

	screen.fill((0,0,0))
	snake.checkCollision()
	snake.checkFood(food)
	snake.show()
	food.show()
	pygame.display.update()
	clock.tick(10)
