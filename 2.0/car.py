class Car:
	#lock...Lenkeinschlag
	def __init__ (mass,power,currentSpeed,maxSpeed,x,y,currentLock, maxLock, orientation):
		self.mass = mass
		self.power = power
		self.currSpeed = currentSpeed
		self.maxSpeed = maxSpeed
		self.x = x
		self.y = y
		self.currLock = currentLock
		self.maxLock = maxLock
		self.orientation = orientation
	
	def updatePosition(self,newX,newY,newAngle):
		self.x = newX
		self.y = newY
		self.orientation = newAngle
	
	def nextPos(time):
		