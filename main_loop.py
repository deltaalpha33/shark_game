class Entity():
	
	def __init__(self, xCord, yCord, texturePath, collisionRadius):
		self.xCord = xCord
		self.yCord = yCord
		self.texturePath = texturePath
		self.collisionRadius = collisionRadius

	def hit(self, gameState):
		pass

	def move(self):
		self.xCord += 1

	def display(self):
		pass


class Checkpoint():
	def __init__(self, textToDisplay):
		self.textToDisplay = textToDisplay

	def enter():
		pass

class GameState():
	def __init__(self):
		#each stage unlocks an entitiy
		#fish, pollution, boat
		self.possibleEntities = list(False, False, False)
		self.timeCounter = 0
		self.hp = 100
		self.isEnd = False
		self.entityList = list()
		self.checkpointList = list()

		#shark is just a position on the y axis
		self.sharkPos = 0

	def updateMotionBar(self):
		"""checks if there is a new checkpoint, and enters it. then it moves the time"""
		self.timeCounter += 1

	def hitShark(self, e):
		"""returns whether the entity hit the shark"""
		pass
	def updateSharkPos(self):
		"""if player moves up, move shark up, if player moves down, move shark down"""
		pass

	def drawState(self):
		pass

	def addNewEntities(self):
		pass


gameState = GameState()
while(not gameStae.isEnd):
	gameState.updateSharkPos()
	gameState.updateMotionBar()
	for e in gameState.entityList:
		e.move()
		if(gameState.hitShark(e)): #checks to see if entity hit the shark
			e.hit(gameState)

	gameState.addNewEntities()

	gameState.move()
	gameState.drawState()