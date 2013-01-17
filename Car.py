class Car:

    def __init__(self, x, y, sizeX, sizeY, maxSpeed, maxAcceleration, maxNegAcceleration):
        self.speed = 0 #current speed
        self.acceleration = 0 #current acceleration
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.maxSpeed = maxSpeed #max possible speed
        self.maxAcceleration = maxAcceleration
        self.maxNegAcceleration = maxNegacceleration
