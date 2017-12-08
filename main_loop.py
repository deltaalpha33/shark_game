import sys, pygame

class Entity():
	
	def __init__(self, xCord, yCord, collisionRadius):
		self.xCord = xCord
		self.yCord = yCord
		self.collisionRadius = collisionRadius

		

	def hit(self, gameState):
		pass

	def move(self):
		self.xCord -= 1

	def display(self):
		pass

class Fish(Entity):
	def __init__(self, xCord, yCord, collisionRadius):
		super().__init__(xCord, yCord, collisionRadius)
		self.imSurface = pygame.image.load("fish.jpg")

	def hit(self, gameState):
		gameState.score += 1

	def display(self, screen):
		blt(screen, self.imSurface, self.xCord, self.yCord)

class Checkpoint():
	def __init__(self, textToDisplay):
		self.textToDisplay = textToDisplay

	def enter():
		pass

class GameState():
	def __init__(self):
		#each stage unlocks an entitiy
		#fish, pollution, boat
		self.possibleEntities = [False, False, False]
		self.timeCounter = 0
		self.hp = 100
		self.score = 0
		self.isEnd = False
		self.entityList = list()
		self.checkpointList = list()

		#shark is just a position on the y axis
		self.sharkPos = 0


		#initialize pygame

		pygame.init()

		size = self.width, self.height = 1000, 400

		self.screen = pygame.display.set_mode(size)

	def updateTime(self):
		"""checks if there is a new checkpoint, and enters it. then it moves the time"""
		self.timeCounter += 1

	def hitShark(self, e):
		"""returns whether the entity hit the shark"""
		pass
	def updateSharkPos(self, num):
		"""if player moves up, move shark up, if player moves down, move shark down"""
		self.sharkPos += num
		print("shark pos" + str(self.sharkPos))

	def drawState(self):
		for e in self.entityList:
			e.display(pygame.display.get_surface())

	def addNewEntities(self, n=1):
		for x in range(n):
			e = Fish(10, 10 , 1)
			self.entityList.append(e)

	def moveEntities(self):
		for e in self.entityList:
			e.move()


gameState = GameState()
gameState.addNewEntities()
while(not gameState.isEnd):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				#up
				gameState.updateSharkPos(-1)
				
			if event.key == pygame.K_s:
				#down
				gameState.updateSharkPos(1)

	gameState.updateTime()

	for e in gameState.entityList:
		e.move()
		if(gameState.hitShark(e)): #checks to see if entity hit the shark
			e.hit(gameState)

	gameState.addNewEntities()

	gameState.moveEntities()
	gameState.drawState()

	pygame.time.wait(10)